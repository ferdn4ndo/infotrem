<template>
  <the-modal
    :title="title"
    :visible="visible"
    class="AuthModal"
    @close="$emit('close')"
  >
    <toast-messages ref="AuthModalToastMessages" />

    <article
      v-if="currentState === 'login'"
      class="AuthModal-Content"
    >
      <p class="AuthModal-Paragraph AuthModal-Paragraph--bold">
        Ainda não possua uma conta?
        <a
          href="#"
          title="Registrar-se"
          @click="changeState('register')"
        >clique aqui</a>
        para se registrar.
      </p>

      <p class="AuthModal-Paragraph">
        Se você já tem um cadastro na CSC, insira seu e-mail e senha nos campos
        abaixo e clique em "Entrar".
      </p>

      <login-form
        @error="handleError"
        @success="handleSuccess"
      />
    </article>

    <article
      v-if="currentState === 'register'"
      class="AuthModal-Content"
    >
      <p class="AuthModal-Paragraph AuthModal-Paragraph--bold">
        Já possui um cadastro?
        <a
          href="#"
          title="Registrar-se"
          @click="changeState('login')"
        >clique aqui</a>
        para fazer o login.
      </p>

      <p class="AuthModal-Paragraph">
        Se você ainda não tem um cadastro na CSC, preencha os campos abaixo.
        Estes dados serão utilizados em suas inscrições em nossos
        concursos/processos seletivos. Mantenha-os atualizados! Por lei, você é
        responsável pela veracidade dos mesmos.
      </p>

      <register-form
        @error="handleError"
        @success="handleSuccess"
      />
    </article>
  </the-modal>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .AuthModal {
    &-Content {
      padding: 10px 20px;
    }

    &-Paragraph {
      cursor: default;
      text-align: justify;

      margin: 5px 0 10px;

      &--bold {
        font-weight: bold;
      }
    }
  }
</style>

<script>
  import LoginForm from "@/components/forms/LoginForm.vue";
  import RegisterForm from "@/components/forms/RegisterForm.vue";
  import TheModal from "@/components/modals/TheModal";
  import ToastMessages from "@/components/ToastMessages";

  export default {

    components: {
      LoginForm,
      RegisterForm,
      TheModal,
      ToastMessages,
    },

    props: {
      initialState: {
        type: String,
        required: true,
        validator: function(value) {
          return ["login", "register"].indexOf(value) !== -1;
        },
      },

      visible: {
        type: Boolean,
        default: false,
      },
    },
    data() {
      return {
        currentState: this.initialState,
        title: "",
      };
    },

    watch: {
      visible() {
        this.changeState(this.initialState);
      },
    },

    mounted() {
      this.updateTitle();
    },

    methods: {
      handleError(msg) {
        let toasts = this.$refs.AuthModalToastMessages;
        toasts.addMessage(msg, "error", "error", 10);
      },

      handleSuccess(msg) {
        this.$emit("alert", { text: msg, style: "success", expSecs: 3 });
        this.$emit("close");
      },

      changeState(newState) {
        if (["login", "register"].indexOf(newState) === -1) {
          return false;
        }

        this.currentState = newState;
        this.updateTitle();

        let element = document.getElementsByClassName("TheModal-Content")[0];
        element.scrollTop = 0;
      },

      updateTitle() {
        let mapping = {
          login: "Entre",
          register: "Cadastre-se",
        };

        this.title = mapping[this.currentState];
      },
    },
  };
</script>
