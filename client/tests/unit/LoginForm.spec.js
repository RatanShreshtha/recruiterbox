import { shallowMount, createLocalVue } from "@vue/test-utils";

import { createRenderer } from "vue-server-renderer";

import Vuex from "vuex";
import VueRouter from "vue-router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import createPersistedState from "vuex-persistedstate";

import LoginForm from "@/components/LoginForm.vue";

const localVue = createLocalVue();

localVue.use(Vuex);
localVue.use(VueRouter);

localVue.use(BootstrapVue);
localVue.use(IconsPlugin);

describe("LoginForm.vue", () => {
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
        plugins: [createPersistedState()],
        state
      });
    });

    it("matches snapshot", () => {
      const renderer = createRenderer();

      const wrapper = shallowMount(LoginForm, {
        store,
        localVue
      });

      renderer.renderToString(wrapper.vm, (err, str) => {
        if (err) throw new Error(err);
        expect(str).toMatchSnapshot();
      });
    });
  });
});
