<template>
  <article class="CscHome">
    <section class="CscHome-Section">
      <banner-carousel
        :slides="slides"
        :interval="10000"
        class="CscHome-BannerCarousel"
      />
    </section>

    <section
      v-if="eventsOpenCount > 0"
      class="CscHome-Section"
    >
      <the-title
        class="CscHome-Title"
      >Inscri&ccedil;&otilde;es abertas</the-title>

      <div class="CscHome-CardList">
        <div
          v-for="event in eventsOpen"
          :key="event.id"
          class="CscHome-CardWrapper"
        >
          <event-card
            :event="event"
            class="CscHome-Card"
          />
        </div>
      </div>
    </section>

    <section
      v-if="eventsOngoingCount > 0"
      class="CscHome-Section"
    >
      <the-title class="CscHome-Title">Em Andamento</the-title>

      <div class="CscHome-CardList">
        <div
          v-for="event in eventsOngoing"
          :key="event.id"
          class="CscHome-CardWrapper"
        >
          <event-card
            :event="event"
            class="CscHome-Card"
          />
        </div>
      </div>
    </section>

    <section
      v-if="eventsClosedCount > 0"
      class="CscHome-Section"
    >
      <the-title class="CscHome-Title">Finalizados</the-title>

      <div class="CscHome-CardList">
        <div
          v-for="event in eventsClosed"
          :key="event.id"
          class="CscHome-CardWrapper"
        >
          <event-card
            :event="event"
            class="CscHome-Card"
          />
        </div>
      </div>
    </section>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .CscHome {
    &-BannerCarousel {
      height: 300px;

      max-height: 100vh;
    }

    &-Title {
      margin: 15px 20px;
    }

    &-CardList {
      width: 100%;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      box-sizing: border-box;
      padding: 0 10px;

      &:after {
        content: "";
        flex: auto;
      }
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
        max-width: 33.333%;
      }
    }

    &-Card {
      margin: 0;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import BannerCarousel from "@/components/BannerCarousel";
  import TheTitle from "@/components/TheTitle";
  import EventCard from "@/components/EventCard";
  import { FETCH_EVENTS, FETCH_SLIDES } from "@/store/actions.type";

  export default {
    name: "CscHome",

    components: {
      EventCard,
      BannerCarousel,
      TheTitle,
    },

    computed: {
      ...mapGetters([
        "isAuthenticated",
        "eventsOpenCount",
        "eventsOngoingCount",
        "eventsClosedCount",
        "eventsTotalCount",
        "eventsOpen",
        "eventsOngoing",
        "eventsClosed",
        "hasMoreEvents",
        "currentOffset",
        "slides",
      ]),
    },

    mounted() {
      this.$store.dispatch(FETCH_SLIDES);
      this.$store.dispatch(FETCH_EVENTS);
      this.infiniteScrollWatcher();
    },

    beforeDestroy() {
      this.destroyScrollWatcher();
    },

    methods: {
      infiniteScrollAction() {
        let bottomOfWindow =
          document.documentElement.scrollTop + window.innerHeight ===
          document.documentElement.offsetHeight;

        if (bottomOfWindow && this.hasMoreEvents && !this.isLoading) {
          this.$store.dispatch(FETCH_EVENTS);
        }
      },

      infiniteScrollWatcher() {
        window.addEventListener("scroll", this.infiniteScrollAction);
      },

      destroyScrollWatcher() {
        window.removeEventListener("scroll", this.infiniteScrollAction);
      },
    },
  };
</script>
