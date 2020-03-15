<template>
  <b-row cols="3">
    <b-col></b-col>
    <b-col>
      <h1 class="text-center" v-if="kudos.length > 0">{{ heading }}</h1>
      <h1 class="text-center" v-else>{{ placeholder }}</h1>
    </b-col>
    <b-col></b-col>
    <b-col
      v-for="kudo in kudos"
      :key="kudo.id"
      class="my-2"
      style="display: flex"
    >
      <b-card
        :title="kudo.title"
        header-tag="header"
        footer-tag="footer"
        class="h-100 w-100"
      >
        <b-card-text>
          {{ kudo.description | truncate(100) }}
          <router-link :to="{ name: 'KudoDetail', params: { kudoId: kudo.id } }"
            >See More</router-link
          >
        </b-card-text>
        <template v-slot:footer
          >Awarded: {{ kudo.awarded | moment("calendar") }}</template
        >
      </b-card>
    </b-col>
    <b-col></b-col>
    <b-col>
      <b-pagination-nav
        :link-gen="linkGen"
        :number-of-pages="pages"
        align="center"
        class="mt-2"
        use-router
        v-if="kudos.length > 0"
      ></b-pagination-nav>
    </b-col>
    <b-col></b-col>
  </b-row>
</template>

<script>
import { mapState } from "vuex";

import { apiService } from "@/service";
export default {
  name: "KudoList",
  props: {
    listingType: {
      type: String,
      required: true
    },
    heading: {
      type: String
    },
    placeholder: {
      type: String
    }
  },
  computed: {
    ...mapState(["id", "token"]),
    page() {
      return this.$route.query.page || 1;
    }
  },
  watch: {
    page: {
      immediate: true,
      async handler() {
        this.getKudos();
      }
    }
  },
  data() {
    return {
      kudos: [],
      pages: 1,
      perPage: 9
    };
  },
  async mounted() {
    this.getKudos();
  },
  methods: {
    linkGen(pageNum) {
      return pageNum === 1 ? "?" : `?page=${pageNum}`;
    },
    async getKudos() {
      try {
        const resp = await apiService.get(
          `/api/kudos/?${this.listingType}=${this.id}&page=${this.page}`,
          {
            headers: {
              Authorization: `Token ${this.token}`
            }
          }
        );
        this.kudos = resp.data.results;
        this.pages = resp.data.count / this.perPage;
      } catch (error) {
        console.log("error", error);
      }
    }
  }
};
</script>

<style scoped></style>
