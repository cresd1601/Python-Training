from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.apis import UserProfileView, UserViewSet, SignInView, SignUpView

router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # User Profile
    path("profiles/me/", UserProfileView.as_view(), name="user-profile"),
    # User Authentication URLs
    path("auth/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("auth/signin/", SignInView.as_view(), name="signin"),
    path("auth/signup/", SignUpView.as_view(), name="signup"),
]
