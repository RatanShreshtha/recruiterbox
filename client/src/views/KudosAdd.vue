<template>
  <b-container>
    <b-row>
      <b-col></b-col>
      <b-col>
        <KudoForm />
      </b-col>
      <b-col></b-col>
    </b-row>
  </b-container>
</template>

<script>
import KudoForm from "@/components/KudoForm.vue";

export default {
  name: "Login",
  components: {
    KudoForm
  }
};
</script>

<style></style>
