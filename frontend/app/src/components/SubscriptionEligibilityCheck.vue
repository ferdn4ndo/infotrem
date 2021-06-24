<template>
  <div class="SubscriptionEligibilityCheck">
    <status-item
      :status="getStatusStyle(statusBasicInformation)"
      class="SubscriptionEligibilityCheck-StatusItem"
      title="Informações básicas"
    >
      <span v-if="!checked">Ainda não verificado.</span>

      <span v-if="checked && statusBasicInformation">
        Seus dados básicos (nome, e-mail, CPF, RG, endereço e telefone) estão
        corretamente preenchidos!
      </span>

      <span v-if="checked && !statusBasicInformation">
        Por favor, acesse a seção
        <b><a
          href="#"
          @click="openProfile($event)"
        >Meu Perfil</a></b> e confira
        se seu nome, e-mail, CPF, RG, data de nascimento, endereço e telefone
        estão corretamente preenchidos.
      </span>
    </status-item>

    <status-item
      :status="getStatusStyle(statusEventOpenForSubscriptions)"
      class="SubscriptionEligibilityCheck-StatusItem"
      title="Evento com inscrições abertas"
    >
      <span v-if="!checked">Ainda não verificado.</span>

      <span v-if="checked && statusEventOpenForSubscriptions">
        O evento está com inscrições abertas!
      </span>

      <span v-if="checked && !statusEventOpenForSubscriptions">
        O evento para o qual você está tentanto se inscriver não está com
        inscrições abertas!
      </span>
    </status-item>

    <status-item
      :status="getStatusStyle(statusEmailValidated)"
      class="SubscriptionEligibilityCheck-StatusItem"
      title="Verificação de e-mail"
    >
      <span v-if="!checked">Ainda não verificado.</span>

      <span v-if="checked && statusEmailValidated">
        O seu e-mail já foi validado com sucesso!
      </span>

      <span v-if="checked && !statusEmailValidated">
        O seu e-mail ainda não foi validado! Clique aqui para enviar um novo
        e-mail de validação. Lembre-se de conferir a sua caixa de spam! Após
        validar, atualize esta página e tente novamente.
      </span>
    </status-item>

    <status-item
      v-if="showMultipleSubscriptionStatus"
      :status="getStatusStyle(statusNotAlreadySubscribed)"
      class="SubscriptionEligibilityCheck-StatusItem"
      title="Ainda não está inscrito no evento"
    >
      <span v-if="!checked">Ainda não verificado.</span>

      <span v-if="checked && statusNotAlreadySubscribed">
        Você não está inscrito em outra vaga/cargo para este mesmo evento.
      </span>

      <span v-if="checked && !statusNotAlreadySubscribed">
        Você já está inscrito em outra vaga/cargo para este mesmo evento!
      </span>
    </status-item>

    <status-item
      v-if="showSocioeconomicFormStatus"
      :status="getStatusStyle(statusSocioeconomicForm)"
      class="SubscriptionEligibilityCheck-StatusItem"
      title="Formulário socioeconômico"
    >
      <span v-if="!checked">Ainda não verificado.</span>

      <span v-if="checked && statusSocioeconomicForm">
        O seu formulário socio-econômico está corretamente preenchido!
      </span>

      <span v-if="checked && !statusSocioeconomicForm">
        Por favor, acesse a seção
        <b><a
          href="#"
          @click="openProfile($event)"
        >Meu Perfil</a></b> e confira
        se seu formulário socioeconômico está corretamente preenchido.
      </span>
    </status-item>
  </div>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .SubscriptionEligibilityCheck {
    &-StatusItem {
      margin: 10px 15px 0 10px;
      border-radius: 5px;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import StatusItem from "@/components/StatusItem";
  import { CHECK_SUBSCRIPTION_ELIGIBILITY } from "@/store/actions.type";

  export default {
    name: "SubscriptionEligibilityCheck",

    components: {
      StatusItem,
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
    },

    data() {
      return {
        checked: false,
        checkResult: false,
        statusBasicInformation: false,
        statusEventOpenForSubscriptions: false,
        statusEmailValidated: false,
        statusSocioeconomicForm: false,
        statusNotAlreadySubscribed: false,
        showSocioeconomicFormStatus: false,
        showMultipleSubscriptionStatus: false,
      };
    },

    computed: {
      ...mapGetters(["currentUser", "isAuthenticated"]),
    },

    watch: {
      currentUser() {
        this.reset();
      },

      vacancy() {
        this.reset();
      },
    },

    mounted() {
      this.reset();
    },

    methods: {
      openProfile(event) {
        event.preventDefault();
        this.$router.push({ name: "profile" }).catch(() => {});
        this.$emit("close");
      },

      getStatusStyle(task) {
        return task ? "success" : "error";
      },

      parseCheckResponse(data) {
        this.statusBasicInformation = data.checks.profile_basic_data;
        this.statusEventOpenForSubscriptions =
          data.checks.event_open_for_subscriptions;
        this.statusEmailValidated = data.checks.email_validated;
        this.statusSocioeconomicForm = data.checks.socioeconomic_form;
        this.statusNotAlreadySubscribed = data.checks.not_already_subscribed;

        this.showMultipleSubscriptionStatus = !data.conditions
          .event_allow_multiple_subscriptions;
        this.showSocioeconomicFormStatus =
          data.conditions.event_requires_socioeconomic_form;

        this.checkResult =
          this.statusBasicInformation &&
          this.statusEventOpenForSubscriptions &&
          this.statusEmailValidated &&
          (!this.showMultipleSubscriptionStatus ||
            this.statusNotAlreadySubscribed) &&
          (!this.showSocioeconomicFormStatus || this.statusSocioeconomicForm);

        this.$emit("checked", this.checkResult);
      },

      reset() {
        this.currentState = this.initialState;
        this.checked = false;
        this.check();
      },

      check() {
        if (
          this.currentUser === null ||
          typeof this.currentUser === "undefined" ||
          this.vacancy === null ||
          typeof this.vacancy.id === "undefined"
        ) {
          return;
        }

        let payload = {
          candidate: this.currentUser.id,
          vacancy: this.vacancy.id,
        };

        this.$store
          .dispatch(CHECK_SUBSCRIPTION_ELIGIBILITY, payload)
          .then((data) => {
            this.parseCheckResponse(data);
            this.checked = true;
          });
      },
    },
  };
</script>
