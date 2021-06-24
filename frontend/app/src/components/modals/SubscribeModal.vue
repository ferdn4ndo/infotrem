<template>
  <the-modal
    :title="title"
    :visible="visible"
    class="SubscribeModal"
    @close="$emit('close')"
  >
    <div
      v-if="currentState === 'check'"
      class="SubscribeModal"
    >
      <p class="SubscribeModal-Paragraph">
        Antes de se inscrever, precisamos checar se todas as informações
        necessárias estão preenchidas. Por favor, confira a situação (e a
        descrição) dos itens abaixo.
      </p>

      <subscription-eligibility-check
        :event="event"
        :vacancy="vacancy"
        @close="$emit('close')"
        @checked="parseChecked"
      />

      <div class="SubscribeModal-ButtonWrapper">
        <the-button
          v-if="checkResult"
          class="SubscribeModal-Button"
          text="Avançar"
          @click="goToConfirmation"
        />
      </div>
    </div>

    <div
      v-if="currentState === 'confirm'"
      class="SubscribeModal"
    >
      <p class="SubscribeModal-Paragraph">
        Você está a um passo de confirmar sua inscrição! Aproveite para conferir
        os dados apresentados abaixo antes de continuar. Acesse o menu
        <b><a
          href="#"
          @click="openProfile($event)"
        >Meu Perfil</a></b> para
        editar algum dado caso seja necessário.
      </p>

      <subscription-confirmation-data
        :event="event"
        :vacancy="vacancy"
      />

      <p class="SubscribeModal-Paragraph SubscribeModal-Notice">
        <b>IMPORTANTE:</b> Ao clicar em Avançar você estará se inscrevendo no
        evento com os dados fornecidos acima. Você é o único responsável pela
        veracidade dos mesmos. Sua inscrição somente será confirmada após a
        efetivação do pagamento da taxa de inscrição.
      </p>

      <div class="SubscribeModal-ButtonWrapper">
        <the-button
          v-if="checkResult"
          class="SubscribeModal-Button"
          text="Avançar"
          @click="goToPayment"
        />
      </div>
    </div>

    <div
      v-if="currentState === 'payment'"
      class="SubscribeModal"
    >
      <div v-if="showGeneratingBilletMsg()">
        <div class="SubscribeModal-IconWrapper">
          <the-icon
            icon="clock"
            class="SubscribeModal-Icon"
          />
        </div>

        <p class="SubscribeModal-Paragraph">
          O boleto para pagamento da taxa de inscrição está sendo gerado. Este
          processo pode levar algum tempo. Você pode esperar nesta janela até
          que isto seja concluído para visualizar seu boleto ou pode fechá-la e
          continuar utilizando o site enquanto isso. Você também receberá o
          boleto por e-mail.
        </p>
      </div>

      <div v-if="showBilletDownloadMsg()">
        <div class="SubscribeModal-IconWrapper">
          <the-icon
            icon="download"
            class="SubscribeModal-Icon"
          />
        </div>

        <p class="SubscribeModal-Paragraph">
          O seu boleto para pagamento da taxa de inscrição está pronto para
          visualização! Clique no botão abaixo para continuar.
        </p>

        <the-button
          class="SubscribeModal-Button"
          text="Visualizar Boleto"
          @click="downloadBillet()"
        />
      </div>

      <div v-if="showPaymentInstructionsMsg()">
        <p class="SubscribeModal-Paragraph">
          <b>Siga as instruções de pagamento abaixo para efetivar sua
          inscrição:</b>
        </p>

        <p class="SubscribeModal-Paragraph">{{ event.payment_instructions }}</p>
      </div>

      <div v-if="showEffectedMessage()">
        <div class="SubscribeModal-IconWrapper">
          <the-icon
            icon="success"
            class="SubscribeModal-Icon"
          />
        </div>

        <p class="SubscribeModal-Paragraph">
          Sua inscrição foi efetivada com sucesso! Confira o seu menu de
          inscrições e fique atento à(s) data(s) e local(is) de prova. Boa
          sorte!
        </p>

        <the-button
          class="SubscribeModal-Button"
          text="Fechar"
          @click="$emit('close')"
        />
      </div>
    </div>
  </the-modal>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .SubscribeModal {
    &-Button {
    }

    &-ButtonWrapper {
      padding: 10px 15px 0 10px;
      box-sizing: border-box;

      @media screen and (min-width: $tablet-breakpoint - 1) {
        max-width: 250px;
        margin-left: auto;
      }
    }

    &-IconWrapper {
      text-align: center;
      padding: 10px 10px 0 10px;
    }

    &-Icon {
      color: $foreground-primary-color;
      margin-left: auto;
      margin-right: auto;
      font-size: 78px;
    }

    &-Paragraph {
      cursor: default;
      text-align: justify;

      margin: 10px;

      &--bold {
        font-weight: bold;
      }
    }

    &-Notice {
      background-color: $background-tertiary-color;
      border-top: 1px solid $background-tertiary-border;
      border-bottom: 1px solid $background-tertiary-border;
      padding: 10px;
      margin: 10px 0;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import TheModal from "@/components/modals/TheModal";
  import SubscriptionConfirmationData from "@/components/SubscriptionConfirmationData";
  import {
    CREATE_VACANCY_SUBSCRIPTION,
    FETCH_SUBSCRIPTION,
  } from "@/store/actions.type";
  import TheButton from "@/components/TheButton";
  import SubscriptionEligibilityCheck from "@/components/SubscriptionEligibilityCheck";
  import TheIcon from "@/components/TheIcon";

  export default {
    name: "SubscribeModal",

    components: {
      TheIcon,
      SubscriptionEligibilityCheck,
      TheButton,
      TheModal,
      SubscriptionConfirmationData,
    },

    props: {
      vacancy: {
        type: Object,
        required: true,
      },

      event: {
        type: Object,
        required: true,
      },

      initialState: {
        type: String,
        default: "check",
        validator: function(value) {
          return ["check", "confirm", "payment"].indexOf(value) !== -1;
        },
      },

      visible: {
        type: Boolean,
        default: false,
      },
    },

    data() {
      return {
        currentState: "check",
        checkResult: false,
        subscription: null,
      };
    },

    computed: {
      ...mapGetters(["currentUser", "isAuthenticated"]),

      title() {
        switch (this.currentState) {
          case "check":
            return "Pré-inscrição";
          case "confirm":
            return "Confirmação dos dados";
          case "payment":
            return "Pagamento";
          default:
            return "Erro";
        }
      },
    },

    watch: {
      visible(value) {
        if (value) {
          this.reset();
        }
      },
    },

    mounted() {
      if (this.currentUser === null || this.currentUser === "undefined") {
        this.$emit("close");
      }
    },

    methods: {
      openProfile(event) {
        event.preventDefault();
        this.$router.push({ name: "profile" }).catch(() => {});
        this.$emit("close");
      },

      parseChecked(value) {
        this.checkResult = value;
      },

      goToConfirmation() {
        this.currentState = "confirm";
      },

      goToPayment() {
        let payload = { event: this.event, vacancy: this.vacancy };
        this.$store
          .dispatch(CREATE_VACANCY_SUBSCRIPTION, payload)
          .then((data) => {
            this.subscription = data;
            this.currentState = "payment";

            if (
              this.event.generate_billet &&
              data.status === "GENERATING_BILLET"
            ) {
              this.refreshSubscriptionUntilBilletIsGenerated();
            }
          });
      },

      downloadBillet() {
        console.log("ToDo: downloadBillet");
      },

      refreshSubscriptionUntilBilletIsGenerated() {
        if (this.subscription === null) {
          return;
        }

        this.$store
          .dispatch(FETCH_SUBSCRIPTION, this.subscription.id)
          .then((data) => {
            this.subscription = data;

            if (data.status === "GENERATING_BILLET") {
              window.setTimeout(
                this.refreshSubscriptionUntilBilletIsGenerated,
                5000
              );
            }
          });
      },

      nextStep() {
        if (this.currentState === "check") {
          this.currentState = "confirm";
        } else if (this.currentState === "confirm") {
          this.currentState = "payment";
        }
      },

      reset() {
        this.currentState = this.initialState;
      },

      showGeneratingBilletMsg() {
        return (
          this.event.generate_billet &&
          this.subscription.status === "GENERATING_BILLET"
        );
      },

      showBilletDownloadMsg() {
        return (
          this.event.generate_billet &&
          this.subscription.status === "WAITING_PAYMENT"
        );
      },

      showPaymentInstructionsMsg() {
        return (
          !this.event.generate_billet &&
          this.subscription.status === "WAITING_PAYMENT"
        );
      },

      showEffectedMessage() {
        return this.subscription.status === "EFFECTED";
      },
    },
  };
</script>
