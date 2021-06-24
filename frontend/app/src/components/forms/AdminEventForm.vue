<template>
  <base-form
    ref="adminEventForm"
    class="AdminEventForm"
    :initial-values="initialData"
    :fields="fields"
    submit-text="Salvar"
    @error="handleError"
    @submit="handleValidData"
  >
    <!-- Title -->
    <the-field
      ref="event_title"
      :metadata="{
        maxLength: 120,
      }"
      :required="true"
      name="title"
      type="text"
      class="AdminEventForm-Input"
      placeholder="Nome do Evento"
      description="Insira o nome (título principal) do evento. Ele será exibido em diversos lugares do site."
    />

    <!-- Type -->
    <the-field
      ref="event_type"
      :metadata="{
        items: eventTypeOptions,
        initialValue: initialType,
      }"
      name="event_type"
      type="select"
      class="AdminEventForm-Input"
      placeholder="Tipo do Evento"
      description="O tipo do evento que será criado (concurso público, processo seletivo, etc)."
    />

    <!-- Description -->
    <the-field
      ref="event_description"
      :metadata="{
        type: 'textarea',
        maxLength: 5000,
      }"
      :required="true"
      name="description"
      type="text"
      class="AdminEventForm-Input"
      placeholder="Descrição"
      description="Descrição geral do evento. Procure informar sobre a cidade e um resumo das vagas."
    />

    <!-- Notice -->
    <the-field
      ref="event_notice_text"
      :metadata="{
        type: 'textarea',
        maxLength: 5000,
      }"
      name="notice_text"
      type="text"
      class="AdminEventForm-Input"
      placeholder="Texto de Aviso"
      description="Texto de aviso para informar alguma alteração no evento."
    />

    <!-- Published -->
    <the-field
      ref="event_published"
      name="published"
      type="check"
      class="AdminEventForm-Input"
      placeholder="Publicado (visível ao público)"
    />

    <!-- Registration Start Date -->
    <the-field
      ref="event_registration_start_date"
      :required="true"
      name="registration_start_date"
      type="date"
      class="AdminEventForm-Input"
      placeholder="Abertura das Inscrições (dd/mm/aaaa)"
      description="Data de abertura das inscrições do evento."
    />

    <!-- Registration End Date -->
    <the-field
      ref="event_registration_end_date"
      :required="true"
      name="registration_end_date"
      type="date"
      class="AdminEventForm-Input"
      placeholder="Encerramento das Inscrições (dd/mm/aaaa)"
      description="Data de encerramento das inscrições do evento."
    />

    <!-- Payment Limit Date -->
    <the-field
      ref="event_payment_limit_date"
      :required="true"
      name="payment_limit_date"
      type="date"
      class="AdminEventForm-Input"
      placeholder="Limite de Pagamento das Inscrições (dd/mm/aaaa)"
      description="Data limite de abertura das inscrições (abertas até este dia)."
    />

    <!-- Objective Exam Date -->
    <the-field
      ref="event_exam_objective_date"
      name="exam_objective_date"
      type="date"
      class="AdminEventForm-Input"
      placeholder="Prova Teórica (dd/mm/aaaa)"
      description="Data de aplicação da prova teórica."
    />

    <!-- Practical Exam Date -->
    <the-field
      ref="event_exam_practical_date"
      name="exam_practical_date"
      type="date"
      class="AdminEventForm-Input"
      placeholder="Prova Prática (dd/mm/aaaa)"
      description="Data de aplicação da prova prática."
    />

    <!-- Objective Exam Results Date -->
    <the-field
      ref="event_results_objective_date"
      name="results_objective_date"
      type="date"
      class="AdminEventForm-Input"
      placeholder="Divulg. Res. Prova Teórica (dd/mm/aaaa)"
      description="Data de divulgação dos resultados da prova teórica."
    />

    <!-- Practical Exam Results Date -->
    <the-field
      ref="event_results_practical_date"
      name="results_practical_date"
      type="date"
      class="AdminEventForm-Input"
      placeholder="Divulg. Res. Prova Prática (dd/mm/aaaa)"
      description="Data de divulgação dos resultados da prova prática."
    />

    <!-- Final Results Date -->
    <the-field
      ref="event_results_final_date"
      :required="true"
      name="results_final_date"
      type="date"
      class="AdminEventForm-Input"
      placeholder="Divulgação dos Resultados (dd/mm/aaaa)"
      description="Data de divulgação dos resultados finais (aprovados)."
    />

    <!-- End Date -->
    <the-field
      ref="event_end_date"
      :required="true"
      name="end_date"
      type="date"
      class="AdminEventForm-Input"
      placeholder="Encerramento do Evento (dd/mm/aaaa)"
      description="Data de encerramento (finalização) do evento."
    />

    <!-- Generate Billet -->
    <the-field
      ref="event_generate_billet"
      name="generate_billet"
      type="check"
      class="AdminEventForm-Input"
      placeholder="Gerar Boleto"
      @change="changeGenerateBillet"
    />

    <!-- Billet Gateway -->
    <the-field
      v-if="displayBilletGateway"
      ref="event_billet_gateway"
      :metadata="{
        items: billetGatewayOptions,
        initialValue: initialBilletGateway,
      }"
      :required="displayBilletGateway"
      name="type"
      type="select"
      class="AdminEventForm-Input"
      placeholder="Gateway de Pagamento"
      description="Selecione a interface de pagamento que irá gerar o boleto."
    />

    <!-- Payment Instructions -->
    <the-field
      v-if="!displayBilletGateway"
      ref="event_payment_instructions"
      :metadata="{
        type: 'textarea',
        maxLength: 5000,
      }"
      :required="!displayBilletGateway"
      name="payment_instructions"
      type="text"
      class="AdminEventForm-Input"
      placeholder="Instruções de Pagamento"
      description="Informe as instruções de pagamento que serão exibidas durante a inscrição (em caso de depósito ou transferências)."
    />

    <!-- Allow Multiple Vacancy Subscription -->
    <the-field
      ref="event_allow_multiple_vacancy_subscription"
      name="allow_multiple_vacancy_subscription"
      type="check"
      class="AdminEventForm-Input"
      placeholder="Permitir inscrição em múltiplas vagas"
    />

    <!-- Requires Socioeconomic Form -->
    <the-field
      ref="event_requires_socioeconomic_form"
      name="requires_socioeconomic_form"
      type="check"
      class="AdminEventForm-Input"
      placeholder="Requer formulário sócio-econômico preenchido"
    />
  </base-form>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .AdminEventForm {
    &-Input {
      margin-bottom: 5px;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import {
    CREATE_EVENT,
    FETCH_BILLET_GATEWAYS,
    UPDATE_EVENT,
  } from "@/store/actions.type";
  import { EVENT_TYPE_OPTIONS } from "@/common/enums";
  import BaseForm from "@/components/forms/BaseForm";
  import CheckboxField from "@/components/fields/CheckboxField";
  import SelectField from "@/components/fields/SelectField";
  import TextField from "@/components/fields/TextField";
  import TheIcon from "@/components/TheIcon";
  import TheButton from "@/components/TheButton";
  import TheField from "@/components/fields/TheField";

  export default {
    components: {
      TheField,
      BaseForm,
      CheckboxField,
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

      redirectAfterSave: {
        type: Boolean,
        default: true,
      },
    },

    data: () => ({
      eventTypeOptions: EVENT_TYPE_OPTIONS,
      fields: [],
      initialData: {},
      displayBilletGateway: false,
      billetGatewayOptions: [],
      initialBilletGateway: null,
      initialType: null,
    }),

    computed: {
      ...mapGetters(["currentUser", "billetGateways"]),
    },

    watch: {
      event(value) {
        if (value !== null && typeof value !== "undefined") {
          this.initialData = value;
          this.initialBilletGateway = value.billet_gateway;
          this.displayBilletGateway = value.generate_billet;
          this.initialType = value.type;
        }
      },
    },

    mounted() {
      this.updateFields();
      this.updateBilletGateways();
    },

    methods: {
      handleError(error) {
        this.$emit("error", error);
      },

      handleValidData(payload) {

        if (payload.registration_start_date) {
          payload.registration_start_date += "T00:00:00";
        }

        if (payload.registration_end_date) {
          payload.registration_end_date += "T00:00:00";
        }

        if (payload.payment_limit_date) {
          payload.payment_limit_date += "T00:00:00";
        }

        if (payload.exam_objective_date) {
          payload.exam_objective_date += "T00:00:00";
        }

        if (payload.exam_practical_date) {
          payload.exam_practical_date += "T00:00:00";
        }

        if (payload.results_objective_date) {
          payload.results_objective_date += "T00:00:00";
        }

        if (payload.results_practical_date) {
          payload.results_practical_date += "T00:00:00";
        }

        if (payload.results_final_date) {
          payload.results_final_date += "T00:00:00";
        }

        if (payload.end_date) {
          payload.end_date += "T00:00:00";
        }

        let action = CREATE_EVENT;
        let action_text = "criado";
        let data = {
          payload: payload,
        }

        if (this.event !== null && typeof this.event !== "undefined") {
          action = UPDATE_EVENT;
          action_text = "atualizado";
          data.event_id = this.event.id;
        }

        this.$store
          .dispatch(action, data)
          .then((event) => {
            this.$emit("success", `Evento ${action_text} com sucesso!`);

            if (this.redirectAfterSave) {
              this.$router.push({
                name: "admin-event-detail",
                params: { event_id: event.id },
              });
            }
          })
          .catch((error) => {
            console.log(error);
            if (error.response) {
              if (error.response.status === 400) {
                this.$emit(
                  "error",
                  "Existem campos inválidos. Por favor, confira as informações fornecidas e tente novamente."
                );
              } else if (error.response.status === 409) {
                this.$emit(
                  "error",
                  "E-mail já cadastrado! Utilize a opção 'recuperar senha' (a partir da opção 'Entrar') para recuperar seu acesso."
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

      changeGenerateBillet() {
        this.displayBilletGateway = this.$refs.event_generate_billet.getValue();
      },

      updateBilletGateways() {
        if (this.billetGateways.length) {
          this.parseBilletGatewaysList();
          return;
        }

        this.$store
          .dispatch(FETCH_BILLET_GATEWAYS)
          .then(() => this.parseBilletGatewaysList())
          .catch(() => {
            this.$emit(
              "error",
              "Erro ao recuperar a lista de gateways de pagamento!"
            );
          });
      },

      parseBilletGatewaysList() {
        if (!this.billetGateways.length) {
          return [];
        }

        this.billetGatewayOptions = this.billetGateways.map((obj) => {
          return {
            text: `${obj.name} [${obj.type}]`,
            value: obj.id,
          };
        });

        if (this.initialBilletGateway) {
          this.$refs.event_billet_gateway.setValue(this.initialBilletGateway);
        }
      },

      updateFields() {
        let fields = [
          this.$refs.event_title,
          this.$refs.event_type,
          this.$refs.event_description,
          this.$refs.event_notice_text,
          this.$refs.event_published,
          this.$refs.event_registration_start_date,
          this.$refs.event_registration_end_date,
          this.$refs.event_payment_limit_date,
          this.$refs.event_exam_objective_date,
          this.$refs.event_exam_practical_date,
          this.$refs.event_results_objective_date,
          this.$refs.event_results_practical_date,
          this.$refs.event_results_final_date,
          this.$refs.event_end_date,
          this.$refs.event_generate_billet,
          this.$refs.event_billet_gateway,
          this.$refs.event_payment_instructions,
          this.$refs.event_allow_multiple_vacancy_subscription,
          this.$refs.event_requires_socioeconomic_form,
        ];
        fields = fields.filter((field) => field !== undefined);

        if (this.fields.length !== fields.length) {
          this.fields = fields;
        }
      },
    },
  };
</script>
