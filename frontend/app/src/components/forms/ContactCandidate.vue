<template>
  <base-form
    ref="contactCandidateForm"
    :fields="fields"
    @error="handleError"
    @submit="handleValidData"
  >
    <!-- Name -->
    <the-field
      ref="contact_candidate_name"
      :required="true"
      name="name"
      type="text"
      class="ContactCompanyForm-Input"
      placeholder="Nome completo"
      description="Ex: Fulano Beltrano"
    />

    <!-- E-mail -->
    <the-field
      ref="contact_candidate_email"
      :metadata="{
        type: 'email',
      }"
      :required="true"
      name="email"
      type="text"
      class="ContactCompanyForm-Input"
      placeholder="E-mail para contato"
      description="Ex: fulano@email.com"
    />

    <!-- Phone -->
    <the-field
      ref="contact_candidate_phone"
      :metadata="{
        mask: '(##) ####-####?#',
      }"
      name="phone"
      type="number"
      class="ContactCompanyForm-Input"
      placeholder="Celular / Telefone para contato"
      description="Ex: (11) 99999-9999"
    />

    <!-- Message -->
    <the-field
      ref="contact_candidate_message"
      :metadata="{
        type: 'textarea',
        maxLength: 5000,
      }"
      :required="true"
      name="message"
      type="text"
      class="ContactCompanyForm-Input"
      placeholder="Mensagem"
      description="Procure ser claro na sua necessidade."
    />
  </base-form>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .ContactCompanyForm {
    &-Input {
      margin-bottom: 5px;
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
  import { CREATE_CONTACT } from "@/store/actions.type";
  import BaseForm from "@/components/forms/BaseForm";
  import TextField from "@/components/fields/TextField";
  import TheButton from "@/components/TheButton";
  import TheField from "@/components/fields/TheField";

  export default {
    components: {
      TheField,
      BaseForm,
      TextField,
      TheButton,
    },

    props: {},

    data: () => ({
      fields: [],
    }),

    mounted() {
      this.updateFields();
    },

    methods: {
      handleError(error) {
        this.$emit("error", error);
      },

      handleValidData(payload) {
        this.$store
          .dispatch(CREATE_CONTACT, {
            ...payload,
            type: "PF",
          })
          .then(() => {
            this.$emit(
              "success",
              "Mensagem enviada com sucesso! Entraremos em contato em breve :)"
            );
            this.$refs.contactCandidateForm.clear();
          })
          .catch((error) => {
            if (error.response) {
              if (error.response.status === 400) {
                this.$emit(
                  "error",
                  "Existem campos inválidos. Por favor, confira as informações fornecidas e tente novamente."
                );
              } else if (error.response.status === 429) {
                this.$emit(
                  "error",
                  "Por favor, aguarde 1 minuto antes de enviar uma nova mensagem de contato."
                );
              } else {
                // ToDo: save to a log here
                this.$emit(
                  "error",
                  "Ocorreu um erro interno ao processar sua mensagem. Por favor, tente novamente mais tarde."
                );
              }
            }
          });
      },

      updateFields() {
        this.fields = [
          this.$refs.contact_candidate_name,
          this.$refs.contact_candidate_email,
          this.$refs.contact_candidate_phone,
          this.$refs.contact_candidate_message,
        ];

        this.fields = this.fields.filter((field) => field !== undefined);
      },
    },
  };
</script>
