from django.db import models

# Creating the model for our blog posts!

class BlogPost(models.Model):
    ## In real life, we would not like to send the PK to the frontend.
    ## That is, it is preferable to use  models.UUIDField in the models and remove the PK at the serializers. 
    ## I Prefered to maintain the pk just to make it simpler
    
   
    author = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(null=True,blank=True,upload_to='images/')
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.title} - {self.author}"    
    
