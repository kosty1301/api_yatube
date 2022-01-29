from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import (PostViewSet, CommentViewSet, GroupView, GroupDetailView)


router = SimpleRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('groups/', GroupView.as_view()),
    path('groups/<int:pk>/', GroupDetailView.as_view())
]
