from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import PostViewSet, UserViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),  # Automatically includes the routes from the router
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Schema generation endpoint
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI for API documentation
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # ReDoc UI for API documentation
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]