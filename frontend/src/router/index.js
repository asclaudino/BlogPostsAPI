import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
// import CreatePostView from "../views/CreatePost.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/blogpost/:blogPostID",
    name: "blogPost",
    // route level code-splitting
    // this generates a separate chunk (blog-post.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "blog-post" */ "../views/BlogPost.vue"),
    props: true,
  },
  {
    path: "/createpost",
    name: "createPost",
    // route level code-splitting
    // this generates a separate chunk (create-post.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "create-post" */ "../views/CreatePost.vue"),
  },
];

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

export default router;
