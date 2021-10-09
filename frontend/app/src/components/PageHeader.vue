<script setup>

defineProps({
  user: {
    type: Object,
    default() {
      return {
        id:  0,
        name: "Anônimo",
        avatarUrl: "https://img.r7.com/images/anonymous-31052020133259440?dimensions=460x305&resize=460x305&crop=823x545+0+91",
      };
    },
  },
});
</script>

<template>
  <header class="PageHeader">
    <img
      class="PageHeader-Logo"
      :src="user.avatarUrl"
      alt="Logo da InfoTrem"
    >
  </header>
</template>

<style scoped>
  .PageHeader {
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    height: 100px;

    &-Logo {
      margin: 10px 20px;
      height: 50px;
    }
  }
</style>
