<template>
  <base-form
    ref="LoginForm"
    :initial-values="initialData"
    :fields="fields"
    @error="handleError"
    @submit="handleValidData"
  >
    <!-- E-mail -->
    <the-field
      ref="login_email"
      :metadata="{
        type: 'email',
      }"
      :required="true"
      name="email"
      type="text"
      class="LoginForm-Input"
      placeholder="E-mail"
      description="Insira seu e-mail cadastrado (ex: fulano@email.com)"
      @keyup="submitOnEnter"
    />

    <the-field
      ref="login_password"
      :metadata="{
        type: 'password',
      }"
      :required="true"
      name="password"
      type="text"
      class="LoginForm-Input"
      placeholder="Senha"
      description="Insira sua senha"
      @keyup="submitOnEnter"
    />
  </base-form>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .LoginForm {
    &-Input {
      margin-bottom: 10px;
    }
  }
</style>

<script>
  import BaseForm from "@/components/forms/BaseForm";
  import TheField from "@/components/fields/TheField";
  import { LOGIN } from "@/store/actions.type";

  export default {
    components: {
      BaseForm,
      TheField,
    },

    props: {},

    data: () => ({
      fields: [],
      initialData: {},
    }),

    computed: {},

    mounted() {
      this.updateFields();
    },

    methods: {
      handleError(error) {
        this.$emit("error", error);
      },

      handleValidData(payload) {
        this.$store
          .dispatch(LOGIN, payload)
          .then(() => {
            this.$emit("success", "Login efetuado com sucesso!");
          })
          .catch((error) => {
            if (error.response) {
              if (error.response.status === 400) {
                this.$emit(
                  "error",
                  "Existem campos inválidos. Por favor, confira as informações fornecidas e tente novamente."
                );
              } else if (error.response.status === 401) {
                this.$emit(
                  "error",
                  "E-mail e/ou senha inválido(s). Por favor, confira suas credenciais e tente novamente."
                );
              } else if (error.response.status === 429) {
                this.$emit(
                  "error",
                  "Você atingiu o limite de tentativas por minuto. Por favor, aguarde 1 minuto antes de tentar novamente."
                );
              }
            }
          });
      },

      submitOnEnter: function(event) {
        if (event.keyCode === 13) {
          this.$refs.LoginForm.submit();
        }
      },

      updateFields() {
        this.fields = [this.$refs.login_email, this.$refs.login_password];

        this.fields = this.fields.filter((field) => field !== undefined);
      },
    },
  };
</script>
