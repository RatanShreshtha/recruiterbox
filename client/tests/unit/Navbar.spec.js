import { shallowMount, createLocalVue } from "@vue/test-utils";

import { createRenderer } from "vue-server-renderer";

import Vuex from "vuex";
import VueRouter from "vue-router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

import Navbar from "@/components/Navbar.vue";

const localVue = createLocalVue();

localVue.use(Vuex);
localVue.use(VueRouter);

localVue.use(BootstrapVue);
localVue.use(IconsPlugin);

describe("Navbar.vue", () => {
  describe("User is not Logged In", () => {
    let state;
    let store;

    beforeEach(() => {
      state = {
        id: null,
        kudos: 0,
        username: null,
        first_name: null,
        last_name: null,
        email: null,
        token: null
      };

      store = new Vuex.Store({
        state
      });
    });

    it("matches snapshot", () => {
      const renderer = createRenderer();

      const wrapper = shallowMount(Navbar, {
        store,
        localVue
      });

      renderer.renderToString(wrapper.vm, (err, str) => {
        if (err) throw new Error(err);
        expect(str).toMatchSnapshot();
      });
    });
  });

  describe("User is Logged In", () => {
    let actions;
    let router;
    let routes;
    let state;
    let store;

    beforeEach(() => {
      state = {
        id: 1,
        kudos: 3,
        username: "root",
        first_name: "I am",
        last_name: "Root",
        email: "iam.root@example.com",
        token: "cd6ee1b3f55ddf30457276d6d9a9c17ca03f37b0"
      };

      actions = {
        logout: jest.fn()
      };

      routes = [
        {
          path: "/",
          name: "Home"
        }
      ];

      router = new VueRouter({
        routes
      });

      store = new Vuex.Store({
        state,
        actions
      });
    });

    it("matches snapshot", () => {
      const renderer = createRenderer();

      const wrapper = shallowMount(Navbar, {
        router,
        store,
        localVue
      });

      renderer.renderToString(wrapper.vm, (err, str) => {
        if (err) throw new Error(err);
        expect(str).toMatchSnapshot();
      });
    });

    it("log out user when clicked on log out", () => {
      const wrapper = shallowMount(Navbar, {
        router,
        store,
        localVue
      });

      expect(wrapper.vm.$route.path).toBe("/");

      const button = wrapper.find("#logout");

      button.trigger("click");

      expect(wrapper.vm.$route.path).toBe("/");
    });
  });
});
