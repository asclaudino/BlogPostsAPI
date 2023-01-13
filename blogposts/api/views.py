from blogposts.api.serializers import BlogPostSerializer
from blogposts.models import BlogPost
from rest_framework import generics
# from blogposts.api.pagination import SmallSetPagination

class BlogPostListCreateAPIView(generics.ListCreateAPIView):
   queryset = BlogPost.objects.all().order_by("-created_at")
   serializer_class = BlogPostSerializer
   #pagination_class = SmallSetPagination
   
   
class BlogPostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    