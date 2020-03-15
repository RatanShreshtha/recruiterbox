<template>
  <b-container>
    <b-row>
      <b-col></b-col>
      <b-col>
        <LoginForm />
      </b-col>
      <b-col></b-col>
    </b-row>
  </b-container>
</template>

<script>
import LoginForm from "@/components/LoginForm.vue";

export default {
  name: "Login",
  components: {
    LoginForm
  }
};
</script>

<style></style>
