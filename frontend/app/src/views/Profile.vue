<template>
  <section class="Profile">
    <header-background
      :image-src="headerImageSrc"
      :height="300"
      class="Profile-Banner"
      title="Meu Perfil"
    />

    <nav class="Profile-DataSelection">
      <the-button
        :disabled="form === 'basic'"
        width="auto"
        class="Profile-Button"
        @click="setForm('basic')"
      >
        <the-icon 
          icon="basic_data" 
          class="Profile-ButtonIcon"
        />

        <h1 class="Profile-ButtonTitle">Dados Básicos</h1>
      </the-button>

      <the-button
        :disabled="form === 'socioeconomic'"
        width="auto"
        class="Profile-Button"
        @click="setForm('socioeconomic')"
      >
        <the-icon 
          icon="socioeconomic" 
          class="Profile-ButtonIcon"
        />

        <h1 class="Profile-ButtonTitle">Dados Socioeconômicos</h1>
      </the-button>
    </nav>

    <profile-form
      v-if="form === 'basic'"
      class="Profile-Form"
      @error="handleError"
      @success="handleSuccess"
    />

    <socioeconomical-form
      v-if="form === 'socioeconomic'"
      class="Profile-Form"
      @error="handleError"
      @success="handleSuccess"
    />
  </section>
</template>

<style lang="scss" scoped>
  .Profile {
    &-DataSelection {
      display: flex;
      flex-wrap: wrap;
    }

    &-Button {
      flex: 1 1 40%;
      margin: 10px;
      min-width: 250px;

      &--centered {
        margin-left: auto;
        margin-right: auto;
      }
    }

    &-ButtonIcon {
      font-size: 26px;
    }

    &-ButtonTitle {
      display: inline-block;
      font-size: 26px;
      margin: 10px 10px;
    }

    &-Banner {
      width: 100%;
    }

    &-Form {
      box-sizing: border-box;
      margin: 10px;
    }
  }
</style>

<script>
  import HeaderBackground from "@/components/HeaderBackground";
  import EventsList from "@/components/EventsList";
  import ProfileForm from "@/components/forms/ProfileForm";
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";
  import SocioeconomicalForm from "@/components/forms/SocioeconomicalForm";

  export default {
    name: "ViewProfile",

    components: {
      SocioeconomicalForm,
      TheIcon,
      TheButton,
      ProfileForm,
      HeaderBackground,
      EventsList,
    },

    data() {
      return {
        form: "basic",
        headerImageSrc: "/img/backgrounds/csc-03.jpg",
      };
    },

    methods: {
      setForm(newForm) {
        this.form = newForm;
      },

      handleError(msg) {
        this.$emit("alert", { text: msg, style: "error", expSecs: 10 });
      },

      handleSuccess(msg) {
        this.$emit("alert", { text: msg, style: "success", expSecs: 10 });
      },
    },
  };
</script>
