<template>
  <b-navbar toggleable="lg" type="light" variant="light">
    <b-navbar-brand href="/">Recruiterbox Kudos</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav v-if="token">
        <b-nav-item id="kudos-received" href="/kudos-received"
          >Kudos Received</b-nav-item
        >
        <b-nav-item id="kudos-given" href="/kudos-given"
          >Kudos Given</b-nav-item
        >
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-navbar-nav v-if="token">
          <b-nav-item href="/">
            {{ first_name }} {{ last_name }} ({{ username }})
          </b-nav-item>
          <b-nav-item href="/kudo-add" v-if="kudos > 0">
            <b-button size="sm" type="button" variant="outline-info">
              Give Kudo
            </b-button>
          </b-nav-item>
          <b-nav-item href="#" class="mt-auto">
            <b-button
              id="logout"
              size="sm"
              type="button"
              variant="outline-danger"
              @click="processLogout"
            >
              Log Out
            </b-button>
          </b-nav-item>
        </b-navbar-nav>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Navbar",
  computed: {
    ...mapState(["username", "first_name", "last_name", "token", "kudos"])
  },
  methods: {
    ...mapActions(["logout"]),
    async processLogout() {
      this.logout();
    }
  }
};
</script>

<style scoped></style>
