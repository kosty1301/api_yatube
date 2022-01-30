from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import (PostViewSet, CommentViewSet, GroupView, GroupDetailView)

router_v1 = SimpleRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register(r'posts/(?P<post_id>[^/.]+)/comments',
                   CommentViewSet,
                   basename='comment_detail'
                   )

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
    path('v1/groups/', GroupView.as_view()),
    path('v1/groups/<int:pk>/', GroupDetailView.as_view())
]
