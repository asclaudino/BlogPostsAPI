from blogposts.api.views import (BlogPostDetailAPIView,
                                 BlogPostListCreateAPIView)
from django.urls import path

urlpatterns = [
    path("blog-posts/",
         BlogPostListCreateAPIView.as_view(),
         name="blog-posts-list"),
    path("blog-posts/<int:pk>/",
         BlogPostDetailAPIView.as_view(),
         name="blog-post-detail")
]

