import re
import logging

from celery import shared_task
from django_elasticsearch_dsl.registries import registry

# Models
from apps.feeds.models import (
    Notification,
    PostStatistics,
    User,
    Hashtag,
    Post,
)

logger = logging.getLogger(__name__)


@shared_task
def send_notification_task(user_id, message):
    """Send a notification to the user."""
    user = User.objects.get(id=user_id)
    Notification.objects.create(user=user, message=message)


@shared_task
def sync_post_statistics_task(post_statistics_id):
    """Update the Elasticsearch document for the given PostStatistics."""
    post_statistics = PostStatistics.objects.get(id=post_statistics_id)
    registry.update(post_statistics)


@shared_task
def increment_comments_count_task(post_id):
    """Increment the comments_count field in PostStatistics when a new comment is created."""
    post_statistics = PostStatistics.objects.get(post_id=post_id)
    post_statistics.comments_count = post_statistics.comments_count + 1
    post_statistics.save()


@shared_task
def decrement_comments_count_task(post_id):
    """Decrement the comments_count field in PostStatistics when a comment is deleted."""
    post_statistics = PostStatistics.objects.get(post_id=post_id)
    post_statistics.comments_count = post_statistics.comments_count - 1
    post_statistics.save()


@shared_task
def increment_likes_count_task(post_id):
    """Increment the likes count in PostStatistics."""
    post_statistics = PostStatistics.objects.get(post_id=post_id)
    post_statistics.likes_count = post_statistics.likes_count + 1
    post_statistics.save()


@shared_task
def decrement_likes_count_task(post_id):
    """Decrement the likes count in PostStatistics."""
    post_statistics = PostStatistics.objects.get(post_id=post_id)
    post_statistics.likes_count = post_statistics.likes_count - 1
    post_statistics.save()


@shared_task
def extract_and_associate_hashtags_task(post_id):
    """
    Extract hashtags from the post's content and associate them with the post.
    """
    post = Post.objects.get(id=post_id)
    hashtag_pattern = r"#(\w+)"
    hashtags = re.findall(hashtag_pattern, post.content)
    hashtag_objects = []

    for tag in hashtags:
        hashtag_obj, created = Hashtag.objects.get_or_create(name=tag)
        hashtag_objects.append(hashtag_obj)

    post.hashtags.set(hashtag_objects)
