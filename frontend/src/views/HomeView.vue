<template>
  <div class="home">
    <h1>HomePage</h1>
    <button @click="getBlogPosts"> LOAD QUESTIONS</button>
  </div>
</template>

<script>
// @ is an alias to /src

// import axios from "@/common/api.service.js"
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return{
      question: []
    }
  },

methods:{

    async getBlogPosts() {
        // let endpoint = "/api/blog-posts/";
        // let endpoint = "http://127.0.0.1:8000/api/blog-posts/"
        try{
          const response = await axios.get(`/api/blog-posts/`)
          console.log(response);
        } catch(error){
          console.log(error.response);
          alert(error.response.statusText);
        }
      }

  }
}
</script>
