<template>
  <article class="AdminEventSubscriptions">
    <admin-event-toolbar
      :event="event"
      class="AdminEventSubscriptions-Toolbar"
    />

    <the-title
      class="AdminEventSubscriptions-Title"
    >Inscrições do Evento '{{ event.title }}'</the-title>

    <div class="AdminEventSubscriptions-TableWrapper">
      <data-table
        :rows="subscriptions"
        :headers="headers"
        :allow-removal="true"
        class="AdminEventSubscriptions-Table"
        @click="showEventFile"
        @remove="showRemoveConfirmation"
      />
    </div>

    <confirmation-modal
      ref="SubscriptionRemoveConfirmationModal"
      :message="removeConfirmationMessage"
      :visible="removeConfirmationVisible"
      @close="hideRemoveConfirmation"
      @confirm="removeSubscription"
    />
  </article>
</template>

<style lang="scss" scoped>
  .AdminEventSubscriptions {
    &-Toolbar {
      padding: 10px 10px 0 10px;
    }

    &-TableWrapper {
      width: 100%;
      padding: 10px;
      box-sizing: border-box;
    }

    &-Table {
      width: 100%;
    }
  }
</style>

<script>
  import { FETCH_EVENT, FETCH_EVENT_SUBSCRIPTIONS, REMOVE_SUBSCRIPTION } from "@/store/actions.type";
  import { DefaultErrorMessage } from "@/common/messages";
  import { RequireAdminMixin } from "@/common/mixins";
  import AdminEventForm from "@/components/forms/AdminEventForm";
  import DataTable from "@/components/DataTable";
  import TheTitle from "@/components/TheTitle";
  import AdminEventToolbar from "@/components/AdminEventToolbar";
  import ConfirmationModal from "@/components/modals/ConfirmationModal";

  export default {
    name: "AdminEventSubscriptions",

    components: {
      ConfirmationModal,
      AdminEventToolbar,
      AdminEventForm,
      DataTable,
      TheTitle,
    },

    mixins: [RequireAdminMixin],

    data() {
      return {
        event: {},
        subscriptions: [],
        removeConfirmationVisible: false,
        removeConfirmationMessage: "",
        subscriptionToRemove: {},
        headers: [
          {
            title: "Nome",
            field: "candidate.name",
            isLink: true,
            displayCallback: (value) => {
              return value;
            },
          },
          {
            title: "Vaga/Cargo",
            field: "vacancy.job_title",
            isLink: false,
            displayCallback: (value) => {
              return value;
            },
          },
          {
            title: "Status",
            field: "status",
            isLink: false,
            displayCallback: this.displayStatus,
          },
        ],
      };
    },

    beforeMount() {
      this.$store
        .dispatch(FETCH_EVENT, this.$route.params.event_id)
        .then((event) => {
          this.event = event;
        })
        .catch(() => {
          this.$emit("alert", DefaultErrorMessage);
          this.$router.push({ name: "admin-event-list" });
        });

      this.refreshSubscriptions();
    },

    methods: {
      showEventFile(eventFileId) {
        this.$emit("alert", { text: eventFileId, style: "success" });
      },

      showRemoveConfirmation(subscription) {
        this.subscriptionToRemove = subscription;
        this.removeConfirmationMessage = `Deseja realmente continuar? <br> Isto irá remover completamente a inscrição de código <b>${subscription.id}</b> e seus dados relacionados (como os boletos gerados, se existirem).`;
        this.removeConfirmationVisible = true;
      },

      hideRemoveConfirmation() {
        this.removeConfirmationVisible = false;
      },

      removeSubscription() {
        this.$store
          .dispatch(REMOVE_SUBSCRIPTION, this.subscriptionToRemove.id)
          .then(() => {
            this.refreshSubscriptions();
            this.subscriptionToRemove = {};
            this.removeConfirmationVisible = false;
          })
          .catch(() => {
            this.$emit("alert", DefaultErrorMessage);
            this.$router.push({ name: "admin-event-list" });
          });

      },

      displayStatus(value) {
        const mapping = {
          INCOMPLETE: "Incompleta",
          GENERATING_BILLET: "Gerando Boleto",
          WAITING_PAYMENT: "Ag. Pagamento",
          EFFECTED: "Efetivado",
          CANCELLED: "Cancelado",
        };

        return mapping.hasOwnProperty(value) ? mapping[value] : "Desconhecido";
      },

      refreshSubscriptions() {
        this.$store
          .dispatch(FETCH_EVENT_SUBSCRIPTIONS, this.$route.params.event_id)
          .then((data) => {
            this.subscriptions = data.items;
          })
          .catch(() => {
            this.$emit("alert", DefaultErrorMessage);
            this.$router.push({ name: "admin-event-list" });
          });
      },
    },
  };
</script>
