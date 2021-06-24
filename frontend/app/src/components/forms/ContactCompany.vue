<template>
  <base-form
    ref="contactCompanyForm"
    :fields="fields"
    @error="handleError"
    @submit="handleValidData"
  >
    <!-- Company Name -->
    <the-field
      ref="contact_company_name"
      :required="true"
      name="company_name"
      type="text"
      class="ContactCompanyForm-Input"
      placeholder="Nome da empresa"
      description="Insira a razão social da empresa (ex: Empresa Teste LTDA)"
    />

    <!-- CNPJ -->
    <the-field
      ref="contact_company_cnpj"
      :metadata="{
        mask: '##.###.###/####-##',
      }"
      :required="true"
      name="company_cnpj"
      type="number"
      class="ContactCompanyForm-Input"
      description="Número do CNPJ da empresa (ex: 00.000.000/0001-00)"
      placeholder="CNPJ da empresa"
    />

    <!-- Responsible Name -->
    <the-field
      ref="contact_company_responsible_name"
      :required="true"
      name="company_contact_name"
      type="text"
      class="ContactCompanyForm-Input"
      placeholder="Nome do responsável para contato"
      description="Responderemos para esta pessoa (ex: Fulano Beltrano)"
    />

    <!-- Responsible Job Title -->
    <the-field
      ref="contact_company_responsible_job_title"
      name="company_contact_job"
      type="text"
      class="ContactCompanyForm-Input"
      placeholder="Cargo do responsável na empresa"
      description="Ex: Assessor"
    />

    <!-- E-mail -->
    <the-field
      ref="contact_company_email"
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
      ref="contact_company_phone"
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
      ref="contact_company_message"
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
            type: "PJ",
          })
          .then(() => {
            this.$emit(
              "success",
              "Mensagem enviada com sucesso! Entraremos em contato em breve :)"
            );
            this.$refs.contactCompanyForm.clear();
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
          this.$refs.contact_company_name,
          this.$refs.contact_company_cnpj,
          this.$refs.contact_company_responsible_name,
          this.$refs.contact_company_responsible_job_title,
          this.$refs.contact_company_email,
          this.$refs.contact_company_phone,
          this.$refs.contact_company_message,
        ];

        this.fields = this.fields.filter((field) => field !== undefined);
      },
    },
  };
</script>
