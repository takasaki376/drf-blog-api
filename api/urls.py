from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import BlogViewSet ,BlogListView

router = routers.DefaultRouter()
router.register('blog', BlogViewSet, basename='blog')
router.register('bloglist', BlogListView, basename='bloglist')

urlpatterns = [
    path('', include(router.urls)),
]
