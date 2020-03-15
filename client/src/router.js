import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
import KudosGiven from "./views/KudosGiven.vue";
import KudosReceived from "./views/KudosReceived.vue";
import KudosAdd from "./views/KudosAdd";
import KudoDetail from "./views/KudoDetail";
import store from "@/store";

Vue.use(VueRouter);

const userIsNotAuthenticated = (to, from, next) => {
  console.log("inside userIsNotAuthenticated");

  if (!store.state.token) {
    next();
    return;
  }
  next("/kudos-received");
};

const userIsAuthenticated = (to, from, next) => {
  console.log("inside userIsAuthenticated");

  if (store.state.token) {
    next();
    return;
  }
  next("/login");
};

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    beforeEnter: userIsNotAuthenticated
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    beforeEnter: userIsNotAuthenticated
  },
  {
    path: "/kudos-given",
    name: "KudosGiven",
    component: KudosGiven,
    beforeEnter: userIsAuthenticated
  },
  {
    path: "/kudos-received",
    name: "KudosReceived",
    component: KudosReceived,
    beforeEnter: userIsAuthenticated
  },
  {
    path: "/kudo-detail/:kudoId/",
    name: "KudoDetail",
    component: KudoDetail,
    props: true,
    beforeEnter: userIsAuthenticated
  },
  {
    path: "/kudo-add",
    name: "KudosAdd",
    component: KudosAdd,
    beforeEnter: userIsAuthenticated
  },
  {
    path: "*",
    redirect: "KudosReceived",
    beforeEnter: userIsAuthenticated
  }

  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue")
  // }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
