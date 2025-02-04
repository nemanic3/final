from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecommendationViewSet

router = DefaultRouter()
router.register('', RecommendationViewSet, basename='recommendation')

urlpatterns = [
    path('', include(router.urls)),
]
