<template>
  <b-form @submit="onSubmit">
    <b-form-group id="input-group-1" label="User:" label-for="input-1">
      <b-form-select
        id="input-1"
        v-model="user"
        :options="users"
        required
      ></b-form-select>
    </b-form-group>

    <b-form-group id="input-group-2" label="Title:" label-for="input-2">
      <b-form-input
        id="input-2"
        v-model="title"
        type="text"
        required
        placeholder="Enter title"
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-3" label="description:" label-for="input-3">
      <b-form-textarea
        id="input-3"
        v-model="description"
        placeholder="Enter description..."
        rows="7"
        max-rows="10"
      ></b-form-textarea>
    </b-form-group>

    <b-button class="mr-2" type="submit" variant="primary">Give Kudo</b-button>
  </b-form>
</template>
<script>
import router from "@/router";
import swal from "sweetalert";
import { mapState } from "vuex";

import { apiService } from "@/service";

export default {
  data() {
    return {
      user: null,
      title: "",
      description: "",
      message: null,
      error: null,
      users: [{ text: "Select User to give kudos.", value: null }]
    };
  },
  computed: {
    ...mapState(["id", "first_name", "last_name", "username", "token", "kudos"])
  },
  async mounted() {
    this.getUsers();
  },
  methods: {
    async getUsers() {
      try {
        let nextPage = "/api/users/";

        while (nextPage !== null) {
          const resp = await apiService.get(nextPage, {
            headers: {
              Authorization: `Token ${this.token}`
            }
          });
          nextPage = resp.data.next;
          for (let userData of resp.data.results) {
            const userObj = {
              text: `${userData.first_name} ${userData.last_name}`,
              value: `${userData.id}`
            };
            this.users.push(userObj);
          }
        }
      } catch (error) {
        console.log("error", error);
      }
    },
    async onSubmit(evt) {
      evt.preventDefault();
      try {
        const kudoData = {
          title: this.title,
          description: this.description,
          by_user: this.id,
          to_user: this.user
        };
        console.log(kudoData);

        await apiService.post("/api/kudos/", kudoData, {
          headers: {
            Authorization: `Token ${this.token}`
          }
        });

        swal(
          "Kudo is away ...",
          `You now have ${this.kudos - 1} left.`,
          "success"
        ).then(() => {
          this.$store.dispatch("setKudos", this.kudos - 1);
          router.replace("/kudos-given");
        });
      } catch (error) {
        console.log("error", error);
        this.error = error.message;
      }
    }
  }
};
</script>

<style></style>
