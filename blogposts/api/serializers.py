from rest_framework import serializers
from blogposts.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    ## In real life, we would not like to send the PK to the frontend.
    ## That is, it is preferable to use  models.UUIDField in the models and remove the PK here. 
    ## I Prefered to maintain the pk just to make it simpler
    
    class Meta:
        model = BlogPost
        fields="__all__"