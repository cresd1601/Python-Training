import factory
import random

from apps.users.models import User, UserProfile


# Factory for creating User instances
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(
        lambda o: f"testuser{random.randint(1000, 9999)}"
    )  # Ensure a unique username
    email = factory.LazyAttribute(lambda o: f"{o.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password")
    is_staff = False


# Factory for creating UserProfile instances
class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    bio = "Initial bio"
