# Implemented some automated tests for the blogpostsapi
# -------------------------------------------------

# To run the tests, run python manage.py test
#                   at the project root folder

# -------------------------------------------

import json

from blogposts.api.serializers import BlogPostSerializer
from blogposts.models import BlogPost
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BlogPostsAPITestCase(APITestCase):

    def test_registration(self):

        data = {
            "author": "CS Lewis",
            "email":  "CSLewis@Narnia.com",
            "title":  "Aslam",
            "content": "Some random blog post of Lewis"
        }
        response = self.client.post("/api/blog-posts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_blog_posts_list(self):
        data = {}
        response = self.client.get("/api/blog-posts/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_post_details(self):

        data = {
            "author": "CS Lewis",
            "email":  "CSLewis@Narnia.com",
            "title":  "Aslam",
            "content": "Some random blog post of Lewis"
        }
        post_response = self.client.post("/api/blog-posts/", data)
        get_response = self.client.get(
            reverse("blog-post-detail", kwargs={"pk": 1}))
        # print(get_response.status_code)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["author"], "CS Lewis")
        self.assertNotEqual(get_response.data["author"], "Random Author")

    def test_blog_post_update(self):

        data = {
            "author": "CS Lewis",
            "email":  "CSLewis@Narnia.com",
            "title":  "Aslam",
            "content": "Some random blog post of Lewis"
        }
        post_response = self.client.post("/api/blog-posts/", data)
        # get_response = self.client.get(reverse("blog-post-detail",kwargs={"pk":1}))
        # print(get_response.status_code)
        # data = {
        #     "content": "Some random blog post of Lewis UPDATED"
        # }
        put_response = self.client.put(reverse("blog-post-detail", kwargs={"pk": 1}),
                                       {
            "id": 1,
            "author": "CS Lewis",
            "email":  "CSLewis@Narnia.com",
            "title":  "Aslam",
            "content": "Some random blog post of Lewis UPDATED"
        })
        # print(put_response.status_code, "Line 76")
        # self.assertEqual(put_response.data["author"],"CS Lewis")
        # self.assertNotEqual(put_response.data["author"],"Random Author")
        self.assertEqual(json.loads(put_response.content)["content"],
                         "Some random blog post of Lewis UPDATED"
                         )
        self.assertNotEqual(json.loads(put_response.content)["content"],
                         "Some random blog post of Lewis"
                         )
