from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet, AchievementViewSet, LightCatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register('achievements', AchievementViewSet)
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]