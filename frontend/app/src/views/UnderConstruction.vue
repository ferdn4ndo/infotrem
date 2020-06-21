<template>
  <background-carousel>
    <new-title>Fernando <strong>Constantino</strong></new-title>

    <new-footer></new-footer>
  </background-carousel>
</template>

<script>
import BackgroundCarousel from "@/components/BackgroundCarousel";
import NewTitle from "@/components/NewTitle";
import NewFooter from "@/components/NewFooter";

export default {
  components: {
    BackgroundCarousel,
    NewTitle,
    NewFooter
  }
};
</script>
