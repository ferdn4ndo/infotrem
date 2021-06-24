<template>
  <base-form
    ref="adminEventLinkForm"
    class="AdminEventLinkForm"
    :initial-values="initialData"
    :fields="fields"
    submit-text="Salvar"
    @error="handleError"
    @submit="handleValidData"
  >
    <!-- Name -->
    <the-field
      ref="name"
      :metadata="{
        maxLength: 120,
      }"
      :required="true"
      name="name"
      type="text"
      class="AdminEventLinkForm-Input"
      placeholder="Nome do link"
      description="Insira o nome (título) do link."
    />

    <!-- Url -->
    <the-field
      ref="url"
      :metadata="{
        maxLength: 200,
      }"
      :required="true"
      name="url"
      type="text"
      class="AdminEventLinkForm-Input"
      placeholder="URL do link"
      description="Insira a URL (endereço) do link."
    />

    <!-- Visibility -->
    <the-field
      ref="visibility"
      :metadata="{
        items: linkVisibilityOptions,
      }"
      :required="true"
      name="visibility"
      type="select"
      class="AdminEventLinkForm-Input"
      placeholder="Visibilidade do link"
      description="Define quem poderá ver o link"
    />
  </base-form>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .AdminEventLinkForm {
    &-Input {
      margin-bottom: 5px;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { CREATE_EVENT_LINK, UPDATE_EVENT_LINK } from "@/store/actions.type";
  import { EVENT_LINK_VISIBILITY_OPTIONS } from "@/common/enums";
  import BaseForm from "@/components/forms/BaseForm";
  import SelectField from "@/components/fields/SelectField";
  import TextField from "@/components/fields/TextField";
  import TheIcon from "@/components/TheIcon";
  import TheButton from "@/components/TheButton";
  import TheField from "@/components/fields/TheField";

  export default {
    components: {
      TheField,
      BaseForm,
      SelectField,
      TextField,
      TheIcon,
      TheButton,
    },

    props: {
      event: {
        type: Object,
        default: () => {},
      },

      link: {
        type: Object,
        default: () => {},
      },

      redirectAfterSave: {
        type: Boolean,
        default: true,
      },
    },

    data: () => ({
      linkVisibilityOptions: EVENT_LINK_VISIBILITY_OPTIONS,
      fields: [],
      initialData: {},
    }),

    computed: {
      ...mapGetters(["currentUser", "billetGateways"]),
    },

    watch: {
      link(value) {
        if (value !== null && typeof value !== "undefined") {
          this.initialData = value;
        } else {
          this.initialData = {};

          this.fields.forEach((field) => field.clear());
        }
      },
    },

    mounted() {
      this.updateFields();
    },

    methods: {
      handleError(error) {
        this.$emit("error", error);
      },

      handleValidData(payload) {
        let finalPayload = { payload: payload, event_id: this.event.id };
        let actionText = "criado";
        let action = CREATE_EVENT_LINK;

        if (this.link !== null && typeof this.link !== "undefined" && this.link !== {} && "id" in this.link) {
          action = UPDATE_EVENT_LINK;
          actionText = "atualizado";
          finalPayload.link_id = this.link.id;
        }

        this.$store
          .dispatch(action, finalPayload)
          .then((event) => {
            this.$emit("success", `Link ${actionText} com sucesso!`);

            if (this.redirectAfterSave) {
              this.$router.push({
                name: "admin-event-links",
                params: { event_id: event.id },
              });
            }
          })
          .catch((error) => {
            console.log(error);
            console.log(error.response);
            if (error.response) {
              if (error.response.status === 400) {
                this.$emit(
                  "error",
                  "Existem campos inválidos. Por favor, confira as informações fornecidas e tente novamente."
                );
              } else {
                // ToDo: save to a log here
                this.$emit(
                  "error",
                  "Ocorreu um erro interno ao processar seu cadastro. Por favor, entre em contato relatando o problema."
                );
              }
            }
          });
      },

      updateFields() {
        this.fields = [
          this.$refs.name,
          this.$refs.url,
          this.$refs.visibility,
        ];
      },
    },
  };
</script>
