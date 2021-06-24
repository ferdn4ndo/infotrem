<template>
  <article class="CscServices">
    <header-background
      :height="200"
      :image-src="headerImageSrc"
      class="CscServices-Header"
      title="Política de Privacidade"
    />

    Em construção
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .CscServices {
    width: 100%;

    &-Header {
      margin-bottom: 10px;
    }

    &-Title {
      margin: 15px 20px;
    }
  }
</style>

<script>
  import HeaderBackground from "@/components/HeaderBackground";
  import EventsList from "@/components/EventsList";

  export default {
    name: "ViewPrivacyPolicy",

    components: {
      HeaderBackground,
      EventsList,
    },

    data() {
      return {
        headerImageSrc: "/img/backgrounds/csc-03.jpg",
      };
    },
  };
</script>
