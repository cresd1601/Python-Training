from django.db import models

# Models
from apps.users.models import User
from django_extensions.db.models import TimeStampedModel
from django_softdelete.models import SoftDeleteModel


class Notification(TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"


class CategoryQuerySet(models.QuerySet):
    """Custom queryset for Category model to handle specific queries."""

    def active(self):
        """Return active (non-soft-deleted) posts."""
        return self.filter(deleted_at__isnull=True)


class CategoryManager(models.Manager):
    """Custom manager for handling `Category` related operations."""

    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()


class Category(TimeStampedModel, SoftDeleteModel):
    """Represents a category for categorizing posts."""

    name = models.CharField(max_length=100, unique=True)

    # Custom manager to handle queryset methods
    objects = CategoryManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return self.name


class Hashtag(models.Model):
    """Represents a hashtag that can be associated with posts."""

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Hashtag"
        verbose_name_plural = "Hashtags"
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return self.name


class PostQuerySet(models.QuerySet):
    """Custom queryset for Post model to handle specific queries."""

    def active(self):
        """Filter active (non-soft-deleted) posts."""
        return self.filter(deleted_at__isnull=True)


class PostManager(models.Manager):
    """Custom manager for handling `Post` related operations."""

    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()


class Post(TimeStampedModel, SoftDeleteModel):
    """Represents a blog post or an article with content and associated categories/hashtags."""

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.SET_DEFAULT, default=None)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(
        null=True, blank=True, decimal_places=15, max_digits=19, default=0
    )
    longitude = models.DecimalField(
        null=True, blank=True, decimal_places=15, max_digits=19, default=0
    )

    # Custom manager to handle queryset methods
    objects = PostManager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"Post by {self.user.username} - {self.title}"

    @property
    def author(self):
        """Return the author's username."""
        return self.user.username

    @property
    def location(self):
        """Return the location indexing data for Elasticsearch."""
        return {
            "lat": self.latitude,
            "lon": self.longitude,
        }

    @property
    def likes_count(self):
        """Return the likes count from the related PostStatistics model."""
        return self.statistics.likes_count if self.statistics else 0

    @property
    def comments_count(self):
        """Return the comments count from the related PostStatistics model."""
        return self.statistics.comments_count if self.statistics else 0


class PostStatistics(SoftDeleteModel):
    """Holds statistics for a given post, such as likes and comments count."""

    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        related_name="statistics",
    )

    class Meta:
        verbose_name = "Post Statistics"
        verbose_name_plural = "Post Statistics"
        indexes = [
            models.Index(fields=["likes_count"]),
            models.Index(fields=["comments_count"]),
        ]

    def __str__(self):
        return f"Statistics for {self.post.title}"


class CommentQuerySet(models.QuerySet):
    def active(self):
        """Filter active (non-soft-deleted) comments."""
        return self.filter(deleted_at__isnull=True)


class CommentManager(models.Manager):
    def get_queryset(self):
        return CommentQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()


class Comment(TimeStampedModel, SoftDeleteModel):
    """Represents a comment on a post made by a user."""

    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    # Custom manager to handle queryset methods
    objects = CommentManager()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"


class Like(TimeStampedModel):
    """Represents a like on a post made by a user."""

    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return f"{self.user} likes {self.post}"
