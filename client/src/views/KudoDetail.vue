<template>
  <b-container class="p-4" fluid>
    <b-jumbotron>
      <template v-slot:header>
        {{ kudo.title }}
        <hr class="my-4" />
      </template>

      <template v-slot:lead>
        <div class="row">
          <div class="col-4 text-left">
            <strong>From: </strong>{{ kudo.by_user.first_name }}
            {{ kudo.by_user.last_name }} ({{ kudo.by_user.username }})
          </div>
          <div class="col-4 text-center">
            <strong>To: </strong>{{ kudo.to_user.first_name }}
            {{ kudo.to_user.last_name }} ({{ kudo.to_user.username }})
          </div>
          <div class="col-4 text-right">
            {{ kudo.awarded | moment("calendar") }}
          </div>
        </div>
        <br />
        {{ kudo.description }}
      </template>
    </b-jumbotron>
  </b-container>
</template>

<script>
import { mapState } from "vuex";

import { apiService } from "@/service";
export default {
  name: "KudoDetail",
  computed: {
    ...mapState(["token"])
  },
  props: {
    kudoId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      kudo: null
    };
  },
  async mounted() {
    this.getKudo();
  },
  methods: {
    async getKudo() {
      try {
        const resp = await apiService.get(`/api/kudos/${this.kudoId}`, {
          headers: {
            Authorization: `Token ${this.token}`
          }
        });
        this.kudo = resp.data;
      } catch (error) {
        console.log("error", error);
      }
    }
  }
};
</script>

<style scoped></style>
