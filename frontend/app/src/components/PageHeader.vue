<script setup>
import TextField from './fields/TextField.vue'

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
      src="../assets/logo_white.png"
      alt="Logo da InfoTrem"
    >


    <div class="PageHeader-Search">
      <text-field
        id="txtSearch"
        name="search"
        placeholder="Buscar (ex: G12; 343589; ZPV; etc...)"
      />
    </div>

    <div class="PageHeader-Profile">
      <img
        class="PageHeader-Logo"
        :src="user.avatarUrl"
        alt="Logo da InfoTrem"
      >
    </div>
  </header>
</template>

<style scoped>
  .PageHeader {
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    height: 40px;
    width: 100vw;
    padding: 0 var(--margin-medium);
    box-sizing: border-box;
    background-color: var(--text-color-secondary-light);
    //border-bottom: 1px solid var(--secondary-color-border);
    border-bottom: 1px solid var(--border-color-secondary);

    &-Logo {
      height: 30px;
    }

    &-Search {
      flex: 1 1 100%;
      padding: 5px 10px;
    }
  }
</style>
