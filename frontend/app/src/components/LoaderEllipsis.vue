<template>
  <div class="LoaderEllipsis LoaderEllipsis--noSelection">
    <div class="LoaderEllipsis-Element"/>

    <div class="LoaderEllipsis-Element"/>

    <div class="LoaderEllipsis-Element"/>

    <div class="LoaderEllipsis-Element"/>
  </div>
</template>

<script>
  export default {
    props: {},
  };
</script>

<style lang="scss" scoped>
  /* Inspired in https://loading.io/css/ */

  $base-size: 32px;

  .LoaderEllipsis {
    display: inline-block;
    position: relative;
    width: #{$base-size * 9.5};
    height: 80px;

    &-Element {
      position: absolute;
      top: 33px;
      width: #{$base-size * 1.5};
      height: #{$base-size * 1.5};
      border-radius: 50%;
      background: #fff;
      animation-timing-function: cubic-bezier(0, 1, 1, 0);
    }

    &-Element:nth-child(1) {
      left: $base-size;
      animation: lds-ellipsis1 0.6s infinite;
    }

    &-Element:nth-child(2) {
      left: $base-size;
      animation: lds-ellipsis2 0.6s infinite;
    }

    &-Element:nth-child(3) {
      left: #{$base-size * 4};
      animation: lds-ellipsis2 0.6s infinite;
    }

    &-Element:nth-child(4) {
      left: #{$base-size * 7};
      animation: lds-ellipsis3 0.6s infinite;
    }

    &--noSelection {
      /* Source: https://stackoverflow.com/questions/826782/how-to-disable-text-selection-highlighting */
      -webkit-touch-callout: none; /* iOS Safari */
      -webkit-user-select: none; /* Safari */
      -khtml-user-select: none; /* Konqueror HTML */
      -moz-user-select: none; /* Old versions of Firefox */
      -ms-user-select: none; /* Internet Explorer/Edge */
      user-select: none; /* Non-prefixed version, currently
                                      supported by Chrome, Edge, Opera and Firefox */
    }

    @keyframes lds-ellipsis1 {
      0% {
        transform: scale(0);
      }
      100% {
        transform: scale(1);
      }
    }
    @keyframes lds-ellipsis3 {
      0% {
        transform: scale(1);
      }
      100% {
        transform: scale(0);
      }
    }
    @keyframes lds-ellipsis2 {
      0% {
        transform: translate(0, 0);
      }
      100% {
        transform: translate(#{$base-size * 3}, 0);
      }
    }
  }
</style>
