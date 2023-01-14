<template>
  <div class="form mt-3">
    <div class="container">
      <form @submit.prevent="onSubmit" enctype="multipart/form-data">
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
        <button type="submit" class="btn btn-primary">Create post</button>
      </form>
      <hr />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CreatePostView",

  data() {
    return {
      author: "",
      email: "",
      photo: null,
      title: "",
      content: "",
      error: null,
    };
  },
  methods: {
    updatePhoto(files) {
      // if(!files.length) return;

      console.log(files[0]);
      //Store the photo
      this.photo = files[0];
    },
    async onSubmit() {
      console.log("form submmited");
      console.log(this.content);
      if (!this.content) {
        this.error = "You can't leave the content empty!";
        return;
      }
      const endpoint = `/api/blog-posts/`;
      try {
        const response = await axios.post(endpoint, {
          author: this.author,
          email: this.email,
          avatar: this.photo,
          title: this.title,
          content: this.content,
        });
        if (this.error) {
          this.error = null;
        }
        alert("Post Created!");
        this.$router.back();
        console.log(response);
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },
  },
};
</script>

<style scoped></style>
