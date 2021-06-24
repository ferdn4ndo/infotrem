<template>
  <article class="Csc404">
    <header-background
      :height="200"
      :image-src="headerImageSrc"
      class="Csc404-Header"
      title="Página não encontrada"
    />

    <section class="Csc404-Content">
      <div class="Csc404-IconWrapper">
        <the-icon 
          class="Csc404-Icon" 
          icon="question"
        />
      </div>

      <h1 class="Csc404-Title">Erro 404</h1>

      <p class="Csc404-Paragraph">
        Não pudemos encontrar a página que você está procurando. Cheque o
        endereço em seu navegador e tente novamente. O link que você usou para
        chegar à esta página também pode estar errado.
      </p>

      <the-button 
        width="auto" 
        class="Csc404-Button" 
        @click="goHome"
      >
        <p class="Csc404-ButtonText">
          Clique aqui para voltar a nossa página incial.
        </p>
      </the-button>
    </section>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .Csc404 {
    width: 100%;

    &-Header {
      margin-bottom: 20px;
    }

    &-Content {
      box-sizing: border-box;
      width: 100%;
      display: flex;
      flex-direction: column;
      padding-right: 20px;
      padding-left: 20px;
      margin-bottom: 20px;
      text-align: center;
    }

    &-IconWrapper {
      margin: 0;
    }

    &-Icon {
      font-size: 200px;
      color: $color-text-error;
    }

    &-Title {
      text-align: center;
      font-size: 26px;
      flex: 1 1 100%;
      margin: 10px;
    }

    &-Paragraph {
      font-size: 20px;
      flex: 1 1 100%;
    }

    &-Button {
      margin: 10px auto;
      padding: 10px 20px;
    }

    &-ButtonText {
      font-size: 22px;
    }
  }
</style>

<script>
  import HeaderBackground from "@/components/HeaderBackground";
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";

  export default {
    name: "Csc404",

    components: {
      TheIcon,
      HeaderBackground,
      TheButton,
    },

    computed: {
      headerImageSrc() {
        return "/img/backgrounds/csc-01.jpg";
      },
    },

    methods: {
      goHome() {
        this.$router.push({ name: "home" }).catch(() => {});
      },
    },
  };
</script>
