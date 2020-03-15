<template>
  <b-container class="p-4" fluid>
    <KudoList
      listingType="by_user"
      heading="Kudos given by you."
      placeholder="You have not given any kudos."
    />
  </b-container>
</template>
<script>
import KudoList from "@/components/KudoList.vue";

export default {
  name: "KudosGiven",
  components: {
    KudoList
  }
};
</script>

<style></style>
