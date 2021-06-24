<template>
  <article class="EventsList">
    <section class="EventsList-Section">
      <the-title>Inscri&ccedil;&otilde;es abertas</the-title>

      <div class="EventsList-CardList">
        <div
          v-for="event in eventsOpen"
          :key="event.id"
          class="EventsList-CardWrapper"
        >
          <event-card
            :event="event"
            class="EventsList-Card"
          />
        </div>
      </div>
    </section>

    <section class="EventsList-Section">
      <the-title>Em Andamento</the-title>

      <div class="EventsList-CardList">
        <div
          v-for="event in eventsOngoing"
          :key="event.id"
          class="EventsList-CardWrapper"
        >
          <event-card
            :event="event"
            class="EventsList-Card"
          />
        </div>
      </div>
    </section>

    <section class="EventsList-Section">
      <the-title>Finalizados</the-title>

      <div class="EventsList-CardList">
        <div
          v-for="event in eventsClosed"
          :key="event.id"
          class="EventsList-CardWrapper"
        >
          <event-card
            :event="event"
            class="EventsList-Card"
          />
        </div>
      </div>
    </section>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .EventsList {
    &-Header {
    }

    &-Section {
      margin: 20px 0;
    }

    &-CardList {
      width: 100%;
      display: flex;
      flex-wrap: wrap;
      //justify-content: space-around;
    }

    &-CardWrapper {
      box-sizing: border-box;
      min-width: 300px;
      max-width: 100%;
      flex: 1 1 auto;
      padding: 10px;

      @media screen and (min-width: $mobile-breakpoint - 1) {
        max-width: 50%;
      }

      @media screen and (min-width: $desktop-breakpoint - 1) {
        max-width: 33%;
      }
    }

    &-Card {
      margin: 0;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import TheTitle from "@/components/TheTitle";
  import EventCard from "@/components/EventCard";
  import { FETCH_EVENTS } from "@/store/actions.type";

  export default {
    components: {
      EventCard,
      TheTitle,
    },

    props: {
      type: {
        type: String,
        default: "all",
        validator: function(value) {
          return (
            ["ALL", "PUBLIC_TENDER", "SELECTION_PROCESS"].indexOf(value) !== -1
          );
        },
      },
    },

    computed: {
      ...mapGetters(["eventsOpen", "eventsOngoing", "eventsClosed"]),
    },

    mounted() {
      if (this.type !== "ALL") {
        this.$store.dispatch(FETCH_EVENTS, { type: this.$route.query.type });
      } else {
        this.$store.dispatch(FETCH_EVENTS);
      }
    },
  };
</script>
