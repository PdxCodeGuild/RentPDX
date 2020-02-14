from django.urls import path, include

from .views import HomeViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('Home', HomeViewSet, basename= 'Home')
router.register('User', UserViewSet, basename='User')
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls))
]
