<template>
  <div class="container mt-3">
    <div v-if="postDetails">
      <h1 class="post-title">
        {{ this.postDetails.title }}
      </h1>
      <p class="post-content">
        {{ this.postDetails.content }}
      </p>
      <p class="mb-0">
        Posted by:
        <span class="post-author"> {{ this.postDetails.author }}</span>
      </p>
      <p class="mb-0">Posted at: {{ this.postDetails.created_at }}</p>
    </div>

    <button v-if="postDetails" @click="toggleIsEditingPost" class="btn btn-outline-success m-3">
      Edit Post Form
    </button>

    <button v-if="postDetails" @click="deletePost" class="btn btn-outline-success m-3">
      Delete Post
    </button>
    <div>
      <div class="container my-2">
        <h1 class="mb-3"></h1>
        <form
          v-if="isEditingPost"
          @submit.prevent="onSubmit"
          enctype="multipart/form-data"
        >
          <div class="mb-3">
            <label for="inputAuthor" class="form-label">Author</label>
            <input
              type="text"
              class="form-control"
              id="inputAuthor"
              aria-describedby="authorHelp"
              v-model="author"
            />
          </div>
          <div class="mb-3">
            <label for="inputEmail" class="form-label">Email address</label>
            <input
              type="email"
              class="form-control"
              id="inputEmail"
              aria-describedby="emailHelp"
              v-model="email"
            />
            <div id="emailHelp" class="form-text">
              We'll never share your email with anyone else.
            </div>
          </div>
          <div class="mb-3">
            <label for="inputImage" class="form-label">Image</label>
            <input
              type="file"
              class="form-control-file"
              id="inputImage"
              accept="image/*"
              @change="updatePhoto($event.target.name, $event.target.files)"
            />
          </div>
          <div class="mb-3">
            <label class="form-label" for="exampleCheck1"> Title</label>
            <input
              type="text"
              class="form-control"
              id="inputTitle"
              aria-describedby="titleHelp"
              v-model="title"
            />
          </div>
          <div class="mb-3">
            <label for="InputContent" class="form-label">Post Content</label>
            <textarea
              placeholder="Share your thoughts!"
              class="form-control"
              id="InputContent"
              rows="3"
              v-model="content"
            ></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Edit post</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "blogPost",
  props: {
    blogPostID: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      author: "",
      email: "",
      photo: null,
      title: "",
      content: "",
      postDetails: null,
      endpoint: "",
      isEditingPost: false,
    };
  },
  methods: {
    toggleIsEditingPost() {
      this.isEditingPost = !this.isEditingPost;
    },

    async onSubmit() {
      console.log("form submmited");
      console.log(this.content);
      if (!this.content) {
        this.error = "You can't leave the content empty!";
        return;
      }
      const endpoint = `/api/blog-posts/${this.blogPostID}/`;
      try {
        const response = await axios.put(endpoint, {
          author: this.author,
          email: this.email,
          avatar: this.photo,
          title: this.title,
          content: this.content,
        });
        if (this.error) {
          this.error = null;
        }
        alert("Post Updated!");
        this.toggleIsEditingPost();
        window.location.reload();
        //this.$router.back();
        console.log(response);
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },
    async deletePost() {
      try {
        const response = await axios.delete(this.endpoint);
        console.log(response);
        alert("Post successfully deleted!");
        this.$router.back();
      } catch (error) {
        console.log(error.response);
        alert("Your post was not deleted!");
      }
    },
    setPageTitle(title) {
      document.title = title;
    },
    prePopulateEditForm() {
      this.author = this.postDetails.author;
      this.email = this.postDetails.email;
      this.photo = this.postDetails.photo;
      this.title = this.postDetails.title;
      this.content = this.postDetails.content;
    },
    async getBlogPostDetail() {
      this.endpoint = `/api/blog-posts/${this.blogPostID}/`;
      try {
        const response = await axios.get(this.endpoint);
        console.log(response);
        this.postDetails = response.data;

        //TODO:
        // On real life this date formating should be put on a helpers file to be reused, not recoded.

        const date = new Date(this.postDetails.created_at);
        this.postDetails.created_at = date.toDateString();
        const title = this.postDetails.title;
        this.setPageTitle(title);
        console.log(this.postDetails);
        this.prePopulateEditForm();
      } catch (error) {
        console.log(error.response);
        const title = "404 - Not Found!";
        this.setPageTitle(title);
        alert(error.response.statusText);
        this.$router.back();
      }
    },
  },
  created() {
    this.getBlogPostDetail();
  },
};
</script>

<style>
.error {
  color: red;
  font-weight: bold;
}

.post-author {
  color: #306bac !important;
}

.post-title {
  font-weight: bold;
  font-size: 150%;
  color: #a8763e;
}
</style>
