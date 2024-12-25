from django.core.management.base import BaseCommand
from random import randint
from apps.feeds.factories import PostFactory, CommentFactory, LikeFactory


class Command(BaseCommand):
    help = "Generate mock posts data with comments and likes using Factory Boy"

    def add_arguments(self, parser):
        parser.add_argument(
            "--num_posts", type=int, default=10, help="Number of posts to create"
        )

    def handle(self, *args, **kwargs):
        num_posts = kwargs["num_posts"]

        # Create mock posts
        posts = PostFactory.create_batch(num_posts)

        # For each post, create random comments and likes
        for post in posts:
            # Create a random number of comments (between 1 to 5)
            num_comments = randint(1, 5)
            for _ in range(num_comments):
                CommentFactory.create(post=post)

            # Create a random number of likes (between 1 to 10)
            num_likes = randint(1, 10)
            for _ in range(num_likes):
                LikeFactory.create(post=post)

            # Optionally, print progress
            self.stdout.write(
                f"Created {num_comments} comments and {num_likes} likes for Post: {post.title}"
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {num_posts} posts with random comments and likes"
            )
        )
