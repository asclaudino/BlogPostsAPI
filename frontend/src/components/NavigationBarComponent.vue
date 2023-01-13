<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary my-navbar">
    <div class="container">
      <router-link class="navbar-brand" :to="{ name: 'home' }"
        >Skyler Blog</router-link
      >

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item my-nav-item">
            <button class="btn btn-outline-success">All Posts</button>
          </li>
          <li class="nav-item my-nav-item">
            <button class="btn btn-outline-success">Create Post</button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavigationBarComponent",
};
</script>

<style scoped>
.my-nav-item {
  padding-right: 1rem;
}
.my-navbar {
  border-bottom: 1px solid #dddddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 150%;
}
.navbar-brand:hover {
  color: #dc3545 !important;
}
</style>
