import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import router from "@/router";
Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    id: null,
    kudos: 0,
    username: null,
    first_name: null,
    last_name: null,
    email: null,
    token: null
  },
  mutations: {
    setUserData(state, data) {
      state.id = data.id;
      state.kudos = data.kudos;
      state.username = data.username;
      state.first_name = data.first_name;
      state.last_name = data.last_name;
      state.email = data.email;
      state.token = data.token;
    },
    setKudos(state, kudos) {
      state.kudos = kudos;
    }
  },
  actions: {
    login({ commit }, data) {
      commit("setUserData", data);
      router.replace("/kudos-received");
    },
    logout({ commit }) {
      commit("setUserData", {
        id: null,
        kudos: 0,
        username: null,
        first_name: null,
        last_name: null,
        email: null,
        token: null
      });
      router.replace("/");
    },
    setKudos({ commit }, kudos) {
      commit("setKudos", kudos);
    }
  },
  modules: {}
});
