<template>
  <article class="AdminEventLinks">
    <admin-event-toolbar
      :event="event"
      class="AdminEventLinks-Toolbar"
    />

    <the-title
      class="AdminEventLinks-Title"
    >Links do Evento '{{ event.title }}'</the-title>

    <div class="AdminEventLinks-TableWrapper">
      <data-table
        :rows="links"
        :headers="headers"
        :allow-removal="true"
        :allow-creation="true"
        class="AdminEventLinks-Table"
        @click="showEventLink"
        @create="showEventLinkModal"
        @remove="showRemoveConfirmation"
      />
    </div>

    <event-link-modal
      :event="event"
      :link-id="linkId"
      :visible="displayEventLinkModal"
      @close="hideEventLinkModal"
    />

    <confirmation-modal
      ref="SubscriptionRemoveConfirmationModal"
      :message="removeConfirmationMessage"
      :visible="removeConfirmationVisible"
      @close="hideRemoveConfirmation"
      @confirm="removeLink"
    />
  </article>
</template>

<style lang="scss" scoped>
  .AdminEventLinks {
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
  import { FETCH_EVENT, REMOVE_EVENT_LINK } from "@/store/actions.type";
  import { DefaultErrorMessage } from "@/common/messages";
  import { RequireAdminMixin } from "@/common/mixins";
  import AdminEventForm from "@/components/forms/AdminEventForm";
  import DataTable from "@/components/DataTable";
  import TheTitle from "@/components/TheTitle";
  import AdminEventToolbar from "@/components/AdminEventToolbar";
  import ConfirmationModal from "@/components/modals/ConfirmationModal";
  import EventLinkModal from "@/components/modals/EventLinkModal";

  export default {
    name: "AdminEventLinks",

    components: {
      EventLinkModal,
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
        links: [],
        headers: [
          {
            title: "Nome",
            field: "name",
            isLink: true,
            displayCallback: (value) => {
              return value;
            },
          },
          {
            title: "Visibilidade",
            field: "visibility",
            isLink: false,
            displayCallback: this.displayLinkVisibility,
          },
          {
            title: "URL",
            field: "url",
            isLink: false,
            displayCallback: this.displayUrl,
          },
        ],
        displayEventLinkModal: false,
        linkId: "",
        linkToRemove: {},
        removeConfirmationVisible: false,
        removeConfirmationMessage: "",
      };
    },

    beforeMount() {
      this.refreshLinksList();
    },

    methods: {
      showEventLink(eventLinkId) {
        this.linkId = eventLinkId;
        this.showEventLinkModal();
      },

      displayUrl(value) {
        const shortened = value.length > 30 ? value.substr(0, 30) + '...' : value;

        return `<a href="${value}" target="_blank" title="Visitar URL">${shortened}</a>`;
      },

      displayLinkVisibility(value) {
        if (value === "EVERYONE") {
          return "Todos (visível publicamente)";
        } else if (value === "SUBSCRIBED") {
          return "Apenas para inscritos";
        } else if (value === "UNLISTED") {
          return "Não listado";
        }

        return "Desconhecido";
      },

      refreshLinksList() {
        this.$store
        .dispatch(FETCH_EVENT, this.$route.params.event_id)
        .then((event) => {
          this.event = event;
          this.links = event.links;
        })
        .catch(() => {
          this.$emit("alert", DefaultErrorMessage);
          this.$router.push({ name: "admin-event-list" });
        });
      },

      showEventLinkModal() {
        this.displayEventLinkModal = true;
      },

      hideEventLinkModal() {
        this.refreshLinksList();
        this.displayEventLinkModal = false;
        this.linkId = "";
      },

      showRemoveConfirmation(link) {
        this.linkId = link.id;
        this.removeConfirmationMessage = `Deseja realmente continuar? <br> Isto irá remover completamente o arquivo de código <b>${link.id}</b>.`;
        this.removeConfirmationVisible = true;
      },

      hideRemoveConfirmation() {
        this.removeConfirmationVisible = false;
        this.linkId = "";
      },

      removeLink() {
        const params = {
          event_id: this.event.id,
          link_id: this.linkId,
        };

        this.$store
          .dispatch(REMOVE_EVENT_LINK, params)
          .then(() => {
            this.$emit("alert", {text: "Link removido com sucesso!", style: "success", expSecs: 3})
            this.refreshLinksList();
            this.linkId = "";
            this.removeConfirmationVisible = false;
          })
          .catch(() => {
            this.$emit("alert", DefaultErrorMessage);
            this.$router.push({ name: "admin-event-list" });
          });

      },
    },
  };
</script>
