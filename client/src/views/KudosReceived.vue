<template>
  <b-container class="p-4" fluid>
    <KudoList
      listingType="to_user"
      heading="Kudos received by you."
      placeholder="You have not received any kudos."
    />
  </b-container>
</template>
<script>
import KudoList from "@/components/KudoList.vue";

export default {
  name: "KudosReceived",
  components: {
    KudoList
  }
};
</script>

<style></style>
