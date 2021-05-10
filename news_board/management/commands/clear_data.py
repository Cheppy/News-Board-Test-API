from django.core.management.base import BaseCommand
from news_board.models import Article


class Command(BaseCommand):
    help = "cleaning up upvotes"

    def handle(self, *args, **options):
        todays_posts = Article.objects.all()

        for post in todays_posts:
            post.amount_of_upvotes = 0
            print(post.amount_of_upvotes)
            post.save()
