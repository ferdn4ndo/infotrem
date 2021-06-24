<template>
  <article class="Event">
    <header-background
      :title="event.title"
      :image-src="headerImageSrc"
      class="Event-Banner"
    />

    <event-detail 
      :event="event" 
      class="Event-Detail" 
      @subscribe="subscribe"
    />

    <subscribe-modal
      ref="subscribeModal"
      :vacancy="vacancy"
      :event="event"
      :visible="showSubscribeModal"
      @close="hideSubscriptionModal"
    />
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .Event {
    width: 100%;

    &-Banner {
      width: 100%;
    }

    &-Detail {
      width: 100%;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { FETCH_EVENT } from "@/store/actions.type";
  import store from "@/store";
  import EventDetail from "@/components/EventDetail";
  import HeaderBackground from "@/components/HeaderBackground";
  import SubscribeModal from "@/components/modals/SubscribeModal";

  export default {
    name: "CscEvent",

    components: {
      SubscribeModal,
      EventDetail,
      HeaderBackground,
    },

    props: {},

    data() {
      return {
        headerImageSrc: "/img/backgrounds/csc-03.jpg",
        showSubscribeModal: false,
        vacancy: {},
      };
    },

    beforeRouteEnter(to, from, next) {
      Promise.all([store.dispatch(FETCH_EVENT, to.params.event_id)]).then(
        () => {
          next();
        }
      );
    },

    computed: {
      ...mapGetters(["events", "currentUser", "isAuthenticated"]),

      event() {
        return this.events.filter((event) => {
          return event.id === this.$route.params.event_id;
        })[0];
      },
    },

    methods: {
      logoAlternativeText() {
        return `Logo do evento ${this.event.title}`;
      },

      subscribe(vacancy) {
        if (this.currentUser === null) {
          this.$emit("show-login");
          return;
        }

        this.vacancy = vacancy;
        this.showSubscribeModal = true;
      },

      hideSubscriptionModal() {
        this.showSubscribeModal = false;
      },
    },
  };
</script>
