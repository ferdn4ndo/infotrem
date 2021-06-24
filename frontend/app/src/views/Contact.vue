<template>
  <article class="CscContact">
    <header-background
      :height="200"
      :image-src="headerImageSrc"
      class="CscContact-Header"
      title="Contato"
    />

    <section 
      v-if="type === ''" 
      class="CscContact-Content"
    >
      <p class="CscContact-Paragraph">
        Para melhor atendê-lo, primeiro precisamos saber quem você é. Por favor,
        selecione abaixo a opção que mais se adequa ao seu caso.
      </p>

      <the-button 
        width="auto" 
        class="CscContact-Button" 
        @click="setType('PJ')"
      >
        <the-icon 
          icon="building" 
          class="CscContact-ButtonIcon"
        />

        <h1 class="CscContact-ButtonTitle">Empresas/Órgãos Públicos</h1>

        <p class="CscContact-ButtonText">
          Clique aqui se você é uma empresa ou órgão público e deseja saber mais
          sobre nossos serviços e/ou solicitar um orçamento.
        </p>
      </the-button>

      <the-button 
        width="auto" 
        class="CscContact-Button" 
        @click="setType('PF')"
      >
        <the-icon 
          icon="user" 
          class="CscContact-ButtonIcon"
        />

        <h1 class="CscContact-ButtonTitle">Candidatos</h1>

        <p class="CscContact-ButtonText">
          Clique aqui se você é um candidato e possui alguma dúvida sobre algum
          de nossos concursos/processos seletivos.
        </p>
      </the-button>
    </section>

    <section 
      v-if="type !== ''" 
      class="CscContact-Content"
    >
      <the-button
        class="CscContact-Back"
        styling="secondary"
        text="Voltar"
        width="auto"
        @click="setType('')"
      />

      <p class="CscContact-Paragraph">
        Preencha o formulário abaixo para entrar em contato. Os campos marcados
        com
        <the-icon 
          icon="asterisk" 
          size="12pt"
        />
        são obrigatórios. Ao final, clique em enviar e aguarde a confirmação
        antes de sair da página.
      </p>

      <contact-company
        v-if="type === 'PJ'"
        class="CscContact-Form"
        @error="handleError"
        @success="handleSuccess"
      />

      <contact-candidate
        v-if="type === 'PF'"
        class="CscContact-Form"
        @error="handleError"
        @success="handleSuccess"
      />
    </section>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .CscContact {
    width: 100%;

    &-Header {
      margin-bottom: 20px;
    }

    &-Back {
      max-width: 200px;
    }

    &-Content {
      box-sizing: border-box;
      width: 100%;
      display: flex;
      flex-direction: column;
      padding-right: 20px;
      padding-left: 20px;
      margin-bottom: 20px;
    }

    &-Paragraph {
      font-size: 20px;
      flex: 1 1 100%;
    }

    &-Button {
      flex: 1 1 100%;
      margin: 10px;
      height: 100px;

      &--centered {
        margin-left: auto;
        margin-right: auto;
      }
    }

    &-ButtonIcon {
      height: 60px;
      width: 60px;
      font-size: 48px;
      padding-top: 10px;
    }

    &-ButtonTitle {
      font-size: 28px;
      margin: 20px 0;
    }

    &-ButtonText {
      font-size: 22px;
    }

    &-Form {
      padding-bottom: 20px;
    }
  }
</style>

<script>
  import HeaderBackground from "@/components/HeaderBackground";
  import TheIcon from "@/components/TheIcon";
  import TextField from "@/components/fields/TextField";
  import TheButton from "@/components/TheButton";
  import ContactCompany from "@/components/forms/ContactCompany";
  import ContactCandidate from "@/components/forms/ContactCandidate";

  export default {
    name: "CscContact",

    components: {
      ContactCandidate,
      ContactCompany,
      TheIcon,
      HeaderBackground,
      TextField,
      TheButton,
    },

    data() {
      return {
        type: "", // will be either 'PF' or 'PJ'
      };
    },

    computed: {
      headerImageSrc() {
        return "/img/backgrounds/csc-01.jpg";
      },
    },

    methods: {
      setType(type) {
        window.scrollTo(0, 0);
        this.type = type;
      },

      handleError(msg) {
        this.$emit("alert", { text: msg, style: "error", expSecs: 10 });
      },

      handleSuccess(msg) {
        this.$emit("alert", { text: msg, style: "success", expSecs: 10 });
        this.$emit("close");
      },
    },
  };
</script>
