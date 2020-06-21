<template>
  <div class="footer-box">
    <ul class="footer-contact">
      <!-- E-mail -->
      <li>
        <icon-link
          url="mailto:const.fernando@gmail.com"
          title="Send an e-mail"
          icon="mail"
        ></icon-link>
      </li>

      <!-- Lattes -->
      <li>
        <icon-link
          url="http://lattes.cnpq.br/0000193480393165"
          title="Lattes CV"
          icon="graduation"
        ></icon-link>
      </li>

      <!-- LinkedIn -->
      <li>
        <icon-link
          url="https://www.linkedin.com/in/fernando-constantino-b5b0aa4a/"
          title="LinkedIn Profile"
          icon="linkedin"
        ></icon-link>
      </li>

      <!-- Instagram -->
      <li>
        <icon-link
          url="https://www.instagram.com/fconstantinophotography/"
          title="Instagram Profile"
          icon="instagram"
        ></icon-link>
      </li>

      <!-- GitHub -->
      <li>
        <icon-link
          url="https://github.com/ferdn4ndo"
          title="GitHub Profile"
          icon="github"
        ></icon-link>
      </li>

      <!-- Curriculum Vitae -->
      <li>
        <icon-link
          url="/FACS_CV_2020_English.pdf"
          title="Curriculum Vitae"
          icon="curriculum"
        ></icon-link>
      </li>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
  @import "@/styles/_variables.scss";

  .footer-box {
    display: block;
    position: fixed;
    bottom: 0;
    box-sizing: border-box;

    margin: 75px 0;
    padding: 15px 0;

    background-color: rgba(0, 0, 0, 0.33);
    width: 100vw;
    text-align: center;

    color: $primary-text-color;

    @media screen and (min-width: $desktop-breakpoint) {
      padding-right: 10vw;
      text-align: right;
    }
  }

  .footer-contact {
    margin: 0;
    padding: 0;
  }

  .footer-box .footer-contact li {
    display: inline-block;
    float: none;
  }

  .footer-box .footer-contact a {
    border: none;
    color: $primary-text-color;
  }

  .footer-box .footer-contact a:hover {
    color: $secondary-text-color;
  }
</style>

<script>
  import IconLink from "@/components/IconLink";

  export default {
    components: {
      IconLink
    }
  };
</script>
