import factory
import decimal
import uuid

# Factories
from apps.users.factories import UserFactory

# Models
from apps.feeds.models import (
    Notification,
    Category,
    Hashtag,
    Post,
    PostStatistics,
    Comment,
    Like,
    User,
)


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notification

    message = factory.Faker("text")
    user = factory.SubFactory(UserFactory)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")


class HashtagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hashtag

    name = factory.LazyAttribute(lambda o: f"#hashtag_{uuid.uuid4().hex[:8]}")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=6)
    content = factory.Faker("paragraph", nb_sentences=3)
    category = factory.SubFactory("apps.feeds.factories.CategoryFactory")
    user = factory.SubFactory("apps.feeds.factories.UserFactory")
    latitude = factory.LazyFunction(lambda: decimal.Decimal("37.7749"))
    longitude = factory.LazyFunction(lambda: decimal.Decimal("-122.4194"))

    @factory.post_generation
    def hashtags(self, create, extracted, **kwargs):
        """
        Post-generation hook to handle the hashtags many-to-many relationship.
        """
        if not create:
            # Skip if the object is not created in the database.
            return

        if extracted:
            # Use provided hashtags if passed during creation.
            self.hashtags.set(extracted)
        else:
            # Create 3 random hashtags if none are provided.
            self.hashtags.set(HashtagFactory.create_batch(3))

    @factory.lazy_attribute
    def category(self):
        return Category.objects.first() or factory.SubFactory(
            "apps.feeds.factories.CategoryFactory"
        )

    @factory.lazy_attribute
    def user(self):
        return User.objects.first() or factory.SubFactory(
            "apps.feeds.factories.UserFactory"
        )

    @factory.post_generation
    def post_statistics(self, create, extracted, **kwargs):
        """Create PostStatistics automatically when a Post is created."""
        if create and not self.statistics:
            PostStatisticsFactory(post=self)


class PostStatisticsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PostStatistics

    post = factory.SubFactory(PostFactory)
    likes_count = factory.Faker("random_number")
    comments_count = factory.Faker("random_number")


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)
    content = factory.Faker("text")


class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Like

    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)
