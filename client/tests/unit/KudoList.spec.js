import { shallowMount, createLocalVue } from "@vue/test-utils";

import { createRenderer } from "vue-server-renderer";

import Vuex from "vuex";
import VueRouter from "vue-router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import createPersistedState from "vuex-persistedstate";

import KudoList from "@/components/KudoList.vue";

const localVue = createLocalVue();

localVue.use(Vuex);
localVue.use(VueRouter);

localVue.use(BootstrapVue);
localVue.use(IconsPlugin);

describe("KudoList.vue", () => {
  let propsData;
  let state;
  let store;
  let routes;
  let router;

  beforeEach(() => {
    propsData = {
      listingType: "by_user"
    };
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

    routes = [
      {
        path: "/",
        name: "Home"
      }
    ];

    router = new VueRouter({
      routes
    });
  });
  it("matches snapshot", () => {
    const renderer = createRenderer();

    const wrapper = shallowMount(KudoList, {
      localVue,
      store,
      propsData,
      router
    });

    renderer.renderToString(wrapper.vm, (err, str) => {
      if (err) throw new Error(err);
      expect(str).toMatchSnapshot();
    });
  });
});
