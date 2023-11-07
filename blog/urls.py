from django.urls import path
from .views import PostList, PostDetail, TagList, TagDetail

urlpatterns = [
    path("posts/", PostList.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("tags/", TagList.as_view(), name="tag_list"),
    path("tags/<int:pk>/", TagDetail.as_view(), name="tag_detail"),
]
