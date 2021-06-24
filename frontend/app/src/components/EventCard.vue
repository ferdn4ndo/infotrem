<template>
  <the-card class="EventCard">
    <header class="EventCard-Header">
      <h1 class="EventCard-HeaderText">
        {{ event.title }}
      </h1>
    </header>

    <div class="EventCard-Dates">
      <date-indicator
        :date="event.registration_start_date"
        icon="calendar_check"
        styling="initial"
        title="Abertura das inscri&ccedil;&otilde;es"
      />

      <date-indicator
        :date="event.registration_end_date"
        icon="calendar_times"
        styling="final"
        title="Encerramento das inscri&ccedil;&otilde;es"
      />

      <date-indicator
        :date="event.results_final_date"
        icon="results_final"
        title="Data da classifica&ccedil;&atilde;o final"
      />
    </div>

    <div 
      v-if="hasNotice()" 
      class="EventCard-Description EventCard-Notice"
    >
      <the-icon 
        icon="info" 
        class="EventCard-NoticeIcon"
      />

      <b>Atualiza&ccedil;&atilde;o:&nbsp;</b>

      <span v-html="event.notice_text" />
    </div>

    <div
      v-if="hasDescription()"
      class="EventCard-Description"
      v-html="event.description"
    />

    <div class="EventCard-Action">
      <the-button
        text="Saiba Mais"
        class="EventCard-Button"
        @click="openEvent()"
      />
    </div>
  </the-card>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .EventCard {
    display: flex;
    flex-wrap: wrap;

    &-Header {
      flex: 0 0 100%;
      padding: 5px 15px;
      text-align: left;
      box-sizing: border-box;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      color: $foreground-light-color;
      background-color: $background-dark-color;
      border-bottom: 1px solid $background-dark-border;
      min-height: 60px;
      display: flex;
    }

    &-HeaderText {
      align-self: center;
      font-size: 18px;
      font-weight: bold;
      margin: 0;
    }

    &-Dates {
      flex: 0 0 100%;
      padding: 10px 5px;
      box-sizing: border-box;
      height: fit-content;
      text-align: center;
      margin-block-start: 0;
      margin-block-end: 0;
      border-bottom: 1px solid $color-background-border;
    }

    &-Description {
      font-size: 16px;
      font-weight: lighter;
      padding: 20px 10px;
      text-align: justify;
      word-wrap: break-word;
      box-sizing: border-box;
      width: 100%;
    }

    &-Notice {
      background-color: $foreground-tertiary-color;
      border-bottom: 1px solid $color-background-border;
    }

    &-NoticeIcon {
      margin-right: 5px;
    }

    &-Action {
      box-sizing: border-box;
      padding: 10px;
      width: 100%;
    }

    &-Button {
      width: 100%;
    }
  }
</style>

<script>
  import DateIndicator from "@/components/DateIndicator";
  import TheCard from "@/components/TheCard";
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";

  export default {
    components: {
      TheIcon,
      DateIndicator,
      TheButton,
      TheCard,
    },

    props: {
      event: {
        type: Object,
        required: true,
      },
    },

    methods: {
      openEvent() {
        this.$router
          .push({ path: `/eventos/${this.event.id}` })
          .catch(() => {});
      },

      hasDescription() {
        return this.event.description && this.event.description !== "";
      },

      hasNotice() {
        return this.event.notice_text && this.event.notice_text !== "";
      },
    },
  };
</script>
