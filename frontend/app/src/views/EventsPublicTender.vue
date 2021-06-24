<template>
  <section class="CscContent">
    <header-background
      :image-src="headerImageSrc"
      class="CscContent-Banner"
      title="Concursos Públicos"
    />

    <events-list 
      class="CscContent-Data" 
      type="PUBLIC_TENDER"
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
    name: "ViewEventsPublicTender",

    components: {
      HeaderBackground,
      EventsList,
    },

    data() {
      return {
        headerImageSrc: "/img/backgrounds/csc-02.jpg",
      };
    },
  };
</script>
