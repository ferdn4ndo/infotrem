<template>
  <section class="CscContent">
    <header-background
      :image-src="headerImageSrc"
      class="CscContent-Banner"
      title="Processos Seletivos"
    />

    <events-list 
      class="CscContent-Data" 
      type="SELECTION_PROCESS"
    />
  </section>
</template>

<style lang="scss" scoped>
  .CscContent {
    &-Banner {
      width: 100%;
    }

    &-Data {
      margin: 20px 0;
    }
  }
</style>

<script>
  import HeaderBackground from "@/components/HeaderBackground";
  import EventsList from "@/components/EventsList";

  export default {
    name: "ViewEventsSelectionProcess",

    components: {
      HeaderBackground,
      EventsList,
    },

    data() {
      return {
        headerImageSrc: "/img/backgrounds/csc-01.jpg",
      };
    },
  };
</script>
