from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
    UpdateAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, renderers
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

class ArticleList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, *args, **kwargs):
        article = request.data
        print(article)
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response(f"success: Article '{article_saved}' created successfully")
        else:
            return Response("bad request")

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        article.delete()
        return Response("Article deleted", status=status.HTTP_204_NO_CONTENT)


class ArticleUpvote(UpdateAPIView):
    queryset = Article.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def put(self, request, *args, **kwargs):
        article = self.get_object()
        article.amount_of_upvotes += 1
        article.save()
        return Response(article.amount_of_upvotes)

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.amount_of_upvotes)


class UpvoteArticle(ArticleDetail):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        article.amount_of_upvotes += 1
        article.save()

        serializer = self.get_serializer(article)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        post = self.request.query_params.get("post")

        if post:
            queryset = queryset.filter(post=post)

        return queryset

    def perform_create(self, serializer):
        return serializer.save()


class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs["pk"])
        comment.delete()
        return Response("comment deleted", status=status.HTTP_204_NO_CONTENT)
