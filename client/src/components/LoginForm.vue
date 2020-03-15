<template>
  <b-form @submit="onSubmit">
    <b-form-group
      id="input-group-1"
      label="Your Username:"
      label-for="input-1"
      description="We'll never share your username with anyone else."
    >
      <b-form-input
        id="input-1"
        v-model="username"
        type="text"
        required
        placeholder="Enter username"
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-2" label="Your Password:" label-for="input-2">
      <b-form-input
        id="input-2"
        v-model="password"
        type="password"
        required
        placeholder="Enter password"
      ></b-form-input>
    </b-form-group>

    <b-button class="mr-2" type="submit" variant="primary">Login</b-button>
  </b-form>
</template>
<script>
import { mapActions } from "vuex";

import { apiService } from "@/service";

export default {
  data() {
    return {
      username: "",
      password: "",
      message: null,
      error: null
    };
  },
  methods: {
    ...mapActions(["login"]),
    async onSubmit(evt) {
      evt.preventDefault();
      try {
        const credentials = {
          username: this.username,
          password: this.password
        };
        console.log(credentials);
        const resp = await apiService.post("/generate-token/", credentials);
        if (resp.data.token !== undefined) {
          const data = {
            id: resp.data.id,
            kudos: resp.data.kudos,
            username: resp.data.username,
            first_name: resp.data.first_name,
            last_name: resp.data.last_name,
            email: resp.data.email,
            token: resp.data.token
          };
          this.login(data);
        }
      } catch (error) {
        console.log("error", error);
        console.log("error", error.data);
        this.error = error.message;
      }
    }
  }
};
</script>

<style></style>
