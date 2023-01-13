from django.contrib import admin
from blogposts.models import BlogPost

# Registering our BlogPost Admin model here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','author','email','avatar','created_at')
    list_filter = ('author','title','created_at')

admin.site.register(BlogPost,BlogPostAdmin)