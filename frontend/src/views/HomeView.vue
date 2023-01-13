<template>
  <div class="home mt-3">
    <div class="container">
      <div v-for="post in posts" :key="post.id">
        <div class="card shadow p-2 mb-4 bg-body rounded">
          <div class="card-body">
            <h1 class="mb-1 post-title">{{ post.title }}</h1>
            <p class="mb-0 ">Posted by: 
              <span class="post-author"> {{ post.author }}</span></p>
            <p class="mb-0">Posted at: {{ post.created_at }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

// import axios from "@/common/api.service.js"
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      posts: [],
    };
  },

  methods: {
    async getBlogPosts() {
      // let endpoint = "/api/blog-posts/";
      // let endpoint = "http://127.0.0.1:8000/api/blog-posts/"
      try {
        const response = await axios.get(`/api/blog-posts/`);
        this.posts = response.data.results;
        this.posts.map((x) => {
          const date = new Date(x.created_at);
          x.created_at = date.toDateString();
        });
        console.log(this.posts);
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },
  },
  created() {
    console.log("created...");
    this.getBlogPosts();
  },
};
</script>

<style scoped>
.post-author {
  color: #306bac !important;
}

.post-title{
  font-weight: bold;
  font-size: 150%;
  color: #a8763e;
}
</style>
