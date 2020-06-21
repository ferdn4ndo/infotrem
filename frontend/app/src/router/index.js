import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      name: "under_construction",
      path: "/",
      component: () => import("@/views/UnderConstruction")
    },
    {
      path: "/12345-old-home",
      component: () => import("@/views/Home"),
      children: [
        {
          path: "",
          name: "home",
          component: () => import("@/views/HomeGlobal")
        },
        {
          path: "my-feed",
          name: "home-my-feed",
          component: () => import("@/views/HomeMyFeed")
        },
        {
          path: "tag/:tag",
          name: "home-tag",
          component: () => import("@/views/HomeTag")
        }
      ]
    },
    {
      name: "login",
      path: "/12345-login",
      component: () => import("@/views/Login")
    },
    {
      name: "register",
      path: "/12345-register",
      component: () => import("@/views/Register")
    },
    {
      name: "settings",
      path: "/12345-settings",
      component: () => import("@/views/Settings")
    },
    // Handle child routes with a default, by giving the name to the
    // child.
    // SO: https://github.com/vuejs/vue-router/issues/777
    {
      path: "/12345-@:username",
      component: () => import("@/views/Profile"),
      children: [
        {
          path: "",
          name: "profile",
          component: () => import("@/views/ProfileArticles")
        },
        {
          name: "profile-favorites",
          path: "favorites",
          component: () => import("@/views/ProfileFavorited")
        }
      ]
    },
    {
      name: "article",
      path: "/12345-articles/:slug",
      component: () => import("@/views/Article"),
      props: true
    },
    {
      name: "article-edit",
      path: "/12345-editor/:slug?",
      props: true,
      component: () => import("@/views/ArticleEdit")
    }
  ]
});
