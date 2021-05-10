from django.urls import path
from django.contrib import admin
from .views import (ArticleDetail, ArticleList, CommentList,
                    ArticleUpvote, CommentDetail)


app_name = "articles"

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("articles/", ArticleList.as_view(), name="articles"),
    path("articles/<int:pk>", ArticleDetail.as_view()),
    path("comments/", CommentList.as_view(), name="comments"),
    path("comments/<int:pk>", CommentDetail.as_view()),
    path("articles/<int:pk>/upvote/", ArticleUpvote.as_view()),
]
