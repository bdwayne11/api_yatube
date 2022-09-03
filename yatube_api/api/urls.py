from django.urls import path, include
from rest_framework import routers

from api.views import GroupViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
