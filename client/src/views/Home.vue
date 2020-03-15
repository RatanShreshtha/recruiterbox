<template>
  <b-container class="p-4">
    <b-jumbotron>
      <template v-slot:header>Recruiterbox Kudos</template>

      <template v-slot:lead>
        A place to appreciate your colleagues for their work, contributions and
        help by giving them kudos.
      </template>

      <hr class="my-4" />

      <p class="lead">
        Just Sign In and start giving kudos to your colleagues.
      </p>

      <b-button variant="primary" href="/login">Login</b-button>
    </b-jumbotron>
  </b-container>
</template>

<script>
export default {
  name: "Home"
};
</script>
