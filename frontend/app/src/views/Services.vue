<template>
  <article class="Services">
    <header-background
      :image-src="headerImageSrc"
      class="Services-Banner"
      title="Nossos Serviços"
    />

    <the-title class="Services-Title">Concursos Públicos</the-title>

    <p class="Services-Paragraph">
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO
    </p>

    <the-title class="Services-Title">Processos Seletivos</the-title>

    <p class="Services-Paragraph">
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO
    </p>

    <the-title class="Services-Title">Cursos</the-title>

    <p class="Services-Paragraph">
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO<br >
      PRECISA COMPLETAR COM TEXTO
    </p>

    <the-title class="Services-Title">Capacitações</the-title>

    <p class="Services-Paragraph">
      Realização de cursos, palestras e formação continuada nas diversas áreas
      da Educação, Saúde, Administração de Empresas Públicas e Privadas.
    </p>

    <p class="Services-Paragraph">
      Alguns dos temas de nossas capacitações:
    </p>

    <ul class="Services-List">
      <li class="Services-ListItem">
        Formação de Professores para níveis de Educação Infantil, Ensino
        Fundamental Ciclo I e II e Ensino Médio;
      </li>
      <li class="Services-ListItem">Alfabetização;</li>
      <li class="Services-ListItem">Formação por Área;</li>
      <li class="Services-ListItem">
        Conhecimento de Informática na Prática de Ensino;
      </li>
      <li class="Services-ListItem">
        Qualidade no Atendimento e Motivação Escolar;
      </li>
      <li class="Services-ListItem">Educação Inclusiva;</li>
      <li class="Services-ListItem">Gestão Escolar;</li>
      <li class="Services-ListItem">O Papel do Secretário Escolar;</li>
      <li class="Services-ListItem">Trabalho em Equipe;</li>
      <li class="Services-ListItem">
        Desenvolvimento de Liderança e Motivação;
      </li>
      <li class="Services-ListItem">Administração de Tempo;</li>
      <li class="Services-ListItem">
        Relações Interpessoais e Ética Profissional;
      </li>
      <li class="Services-ListItem">Empreendedorismo;</li>
      <li class="Services-ListItem">Qualidade no Atendimento ao Cliente;</li>
      <li class="Services-ListItem">Higiene e Segurança no Trabalho;</li>
      <li class="Services-ListItem">Gerenciamento de Conflitos.</li>
    </ul>

    <p class="Services-Paragraph">
      Tem interesse em algum dos nossos serviços? Entre em contato
      <router-link to="/contato">clicando aqui</router-link>.
    </p>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .Services {
    width: 100%;

    &-Banner {
      margin-bottom: 10px;
    }

    &-Title {
      margin: 15px 20px;
    }

    &-Paragraph {
      margin: 15px 30px;
    }

    &-List {
      margin: 15px 30px;
    }
  }
</style>

<script>
  import HeaderBackground from "@/components/HeaderBackground";
  import TheTitle from "@/components/TheTitle";

  export default {
    name: "CscServices",

    components: {
      HeaderBackground,
      TheTitle,
    },

    data() {
      return {
        headerImageSrc: "/img/backgrounds/csc-02.jpg",
      };
    },

    mounted() {},
  };
</script>
