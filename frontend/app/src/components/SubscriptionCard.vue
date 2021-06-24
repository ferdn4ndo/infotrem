<template>
  <the-card class="SubscriptionCard">
    <header class="SubscriptionCard-Header">
      <h1 class="SubscriptionCard-HeaderText">
        {{ getEventTitle() }}
      </h1>
    </header>

    <div class="SubscriptionCard-Info">
      <div class="SubscriptionCard-InfoBlock">
        <b>Data de Inscrição:</b> {{ subscription.created_at | datetime }}
      </div>

      <div class="SubscriptionCard-InfoBlock">
        <b>Vaga/Cargo Pretendido:</b> {{ getJobTitle() }}
      </div>

      <div class="SubscriptionCard-InfoBlock">
        <b>Total de Vagas:</b> {{ subscription.vacancy.total_vacancies }}
      </div>

      <div class="SubscriptionCard-InfoBlock">
        <b>Valor da Inscrição:</b>
        {{ subscription.vacancy.subscription_price | currency }}
      </div>

      <div class="SubscriptionCard-InfoBlock">
        <b>Situação:</b> {{ getSubscriptionStatus() }}
      </div>
    </div>

    <!-- ToDo: Editais -->

    <!-- ToDo: Material de Apoio -->

    <div class="SubscriptionCard-Action">
      <the-button
        text="Ver Mais"
        class="SubscriptionCard-Button"
        @click="openSubscription()"
      />
    </div>
  </the-card>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .SubscriptionCard {
    display: flex;
    flex-wrap: wrap;

    &-Header {
      flex: 0 0 100%;
      padding: 5px 15px;
      text-align: left;
      box-sizing: border-box;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      color: $foreground-light-color;
      background-color: $background-dark-color;
      border-bottom: 1px solid $background-dark-border;
      min-height: 60px;
      display: flex;
    }

    &-HeaderText {
      align-self: center;
      font-size: 14pt;
      font-weight: bold;
      margin: 0;
    }

    &-Action {
      box-sizing: border-box;
      padding: 10px;
      width: 100%;
    }

    &-Button {
      width: 100%;
    }

    &-Info {
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
    }

    &-InfoBlock {
      flex: 1 0 auto;
      padding: 10px;
      border: 1px solid $color-background-border;
      font-size: 12pt;
    }
  }
</style>

<script>
  import { FETCH_EVENT } from "@/store/actions.type";
  import store from "@/store";
  import DateIndicator from "@/components/DateIndicator";
  import TheCard from "@/components/TheCard";
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";

  export default {
    name: "SubscriptionCard",

    components: {
      TheIcon,
      DateIndicator,
      TheButton,
      TheCard,
    },

    props: {
      subscription: {
        type: Object,
        required: true,
      },
    },

    data() {
      return {
        event: null,
      };
    },

    mounted() {
      store
        .dispatch(FETCH_EVENT, this.subscription.vacancy.event)
        .then((event) => {
          console.log(event);
          this.event = event;
        });
    },

    methods: {
      getEventTitle() {
        return this.event !== null ? this.event.title : "";
      },

      getJobTitle() {
        if (this.event === null) {
          return "";
        }

        return this.event.vacancies.filter((vacancy) => {
          return vacancy.id === this.subscription.vacancy.id;
        })[0].job_title;
      },

      openSubscription() {
        this.$router
          .push({ path: `/inscricoes/${this.subscription.id}` })
          .catch(() => {});
      },

      hasDescription() {
        return (
          this.subscription.description && this.subscription.description !== ""
        );
      },

      hasNotice() {
        return (
          this.subscription.notice_text && this.subscription.notice_text !== ""
        );
      },

      getSubscriptionStatus() {
        switch (this.subscription.status) {
          case "INCOMPLETE":
            return "Incompleta";
          case "GENERATING_BILLET":
            return "Boleto sendo gerado";
          case "WAITING_PAYMENT":
            return "Aguardando Pagamento";
          case "EFFECTED":
            return "Confirmada (pagamento recebido)";
          case "CANCELLED":
            return "Cancelada";
          default:
            return "Erro";
        }
      },
    },
  };
</script>
