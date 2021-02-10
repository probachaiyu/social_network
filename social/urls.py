from django.urls import path

from social.views.analytics import AnalyticsViewSet, UserActivityViewSet
from social.views.post import PostViewSet, PostLikeViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:pk>/', PostViewSet.as_view({'post': 'update'})),
    path('posts/<int:pk>/like/', PostLikeViewSet.as_view()),
    path('analytics/', AnalyticsViewSet.as_view()),
    path('user-activity/', UserActivityViewSet.as_view()),
]
