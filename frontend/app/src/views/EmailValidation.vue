<template>
  <article class="CscEmailValidation">
    <header-background
      :height="200"
      :image-src="headerImageSrc"
      class="CscEmailValidation-Header"
      title="Validação de e-mail"
    />

    <section 
      v-if="hadSuccess" 
      class="CscEmailValidation-Content"
    >
      <div class="CscEmailValidation-IconWrapper">
        <the-icon
          class="CscEmailValidation-Icon CscEmailValidation-Icon--success"
          icon="success"
        />
      </div>

      <h1 class="CscEmailValidation-Title">E-mail confirmado!</h1>

      <p class="CscEmailValidation-Paragraph">
        Seu e-mail foi confirmado com sucesso! Agora você já pode se inscrever
        em um de nossos concursos/processos seletivos. Utilize o botão abaixo
        para voltar à página inicial e continuar navegando.
      </p>

      <the-button
        width="auto"
        class="CscEmailValidation-Button"
        @click="goHome"
      >
        <p class="CscEmailValidation-ButtonText">
          Clique aqui para voltar a nossa página incial.
        </p>
      </the-button>
    </section>

    <section 
      v-else 
      class="CscEmailValidation-Content"
    >
      <div class="CscEmailValidation-IconWrapper">
        <the-icon
          class="CscEmailValidation-Icon CscEmailValidation-Icon--error"
          icon="error"
        />
      </div>

      <h1 class="CscEmailValidation-Title">Erro ao confirmar e-mail!</h1>

      <p class="CscEmailValidation-Paragraph">
        Ocorreu um erro ao com o código de confirmação informado para o seu
        e-mail. Por favor, confira o endereço utilizado e tente novamente.
      </p>

      <the-button
        width="auto"
        class="CscEmailValidation-Button"
        @click="goHome"
      >
        <p class="CscEmailValidation-ButtonText">
          Clique aqui para voltar a nossa página incial.
        </p>
      </the-button>
    </section>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .CscEmailValidation {
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

      &--error {
        color: $color-text-error;
      }

      &--success {
        color: $color-text-success;
      }
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
      padding: 0 20px;
    }

    &-ButtonText {
      font-size: 22px;
    }
  }
</style>

<script>
  import { VALIDATE_EMAIL } from "@/store/actions.type";
  import HeaderBackground from "@/components/HeaderBackground";
  import TheIcon from "@/components/TheIcon";
  import TextField from "@/components/fields/TextField";
  import TheButton from "@/components/TheButton";
  import ContactCompany from "@/components/forms/ContactCompany";
  import ContactCandidate from "@/components/forms/ContactCandidate";

  export default {
    name: "CscEmailValidation",

    components: {
      ContactCandidate,
      ContactCompany,
      TheIcon,
      HeaderBackground,
      TextField,
      TheButton,
    },

    data() {
      return {
        hadSuccess: false,
      };
    },

    computed: {
      headerImageSrc() {
        return "/img/backgrounds/csc-03.jpg";
      },
    },

    beforeMount() {
      let params = {
        userId: this.$route.params.user_id,
        hash: this.$route.params.validation_hash,
      };
      this.$store
        .dispatch(VALIDATE_EMAIL, params)
        .then(() => {
          this.hadSuccess = true;
        })
        .catch((error) => {
          if (error.response) {
            if (error.response.status === 403) {
              this.hadSuccess = false;
            } else if (error.response.status === 429) {
              this.$emit("alert", {
                text:
                  "Você atingiu o limite de tentativas de validação por minuto. Por favor, aguarde e tente novamente.",
                style: "error",
                expSecs: 10,
              });
            } else {
              this.$emit("alert", {
                text:
                  "Ocorreu um erro interno ao processar seu e-mail. Por favor, entre em contato relatando o problema.",
                style: "error",
                expSecs: 10,
              });
              // ToDo: save to a log here
            }
          }
        });
    },

    methods: {
      goHome() {
        this.$router.push({ name: "home" }).catch(() => {});
      },

      setType(type) {
        window.scrollTo(0, 0);
        this.type = type;
      },

      handleError(msg) {
        this.$emit("alert", { text: msg, style: "error", expSecs: 10 });
      },

      handleSuccess(msg) {
        this.$emit("alert", { text: msg, style: "success", expSecs: 10 });
        this.$emit("close");
      },
    },
  };
</script>
