<template>
  <article class="CscSubscriptions">
    <header-background
      :height="200"
      :image-src="headerImageSrc"
      class="CscSubscriptions-Header"
      title="Minhas Inscrições"
    />

    <section
      v-if="subscriptions.length === 0"
      class="CscSubscriptions-Content"
    >
      <div class="CscSubscriptions-IconWrapper">
        <the-icon
          icon="exclamation"
          class="CscSubscriptions-Icon"
        />
      </div>

      <p class="CscSubscriptions-Paragraph">
        Você ainda não está inscrito em um de nossos eventos. Vamos mudar isso?
        <a
          href="#"
          @click="goHome"
        >Clique aqui</a> para ir até a página inicial
        e ver nossos concursos/processos seletivos.
      </p>
    </section>

    <section
      v-else
      class="CscSubscriptions-Content"
    >
      <p class="CscSubscriptions-Paragraph">
        Utilize a seção abaixo para acompanhar suas inscrições em nossos
        eventos. Você também pode conferir os editais e materiais de apoio
        disponibilizados em cada um. A opção para geração de 2ª via de boleto
        também pode ser acessada nesta página.
      </p>
    </section>

    <div class="CscSubscriptions-Cards">
      <subscription-card
        v-for="(subscription, index) in subscriptions"
        :key="index"
        :subscription="subscription"
        class="CscSubscriptions-Card"
      />
    </div>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .CscSubscriptions {
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

    &-Paragraph {
      font-size: 20px;
      flex: 1 1 100%;
    }

    &-IconWrapper {
      margin: 0;
    }

    &-Icon {
      font-size: 200px;
      padding-top: 10px;
      color: $color-text-warning;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { FETCH_SUBSCRIPTIONS } from "@/store/actions.type";
  import store from "@/store";
  import HeaderBackground from "@/components/HeaderBackground";
  import TheIcon from "@/components/TheIcon";
  import ContactCompany from "@/components/forms/ContactCompany";
  import ContactCandidate from "@/components/forms/ContactCandidate";
  import SubscriptionCard from "@/components/SubscriptionCard";

  export default {
    name: "CscContact",

    components: {
      SubscriptionCard,
      ContactCandidate,
      ContactCompany,
      TheIcon,
      HeaderBackground,
    },

    beforeRouteEnter(to, from, next) {
      Promise.all([store.dispatch(FETCH_SUBSCRIPTIONS)]).then(() => {
        next();
      });
    },

    data() {
      return {};
    },

    computed: {
      ...mapGetters(["subscriptions", "currentUser", "isAuthenticated"]),
      headerImageSrc() {
        return "/img/backgrounds/csc-03.jpg";
      },
    },

    methods: {
      goHome() {
        this.$router.push({ name: "home" }).catch(() => {});
      },
    },
  };
</script>
