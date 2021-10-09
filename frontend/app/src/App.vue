<script setup>
/*
The code inside is compiled as the content of the component's setup() function.
This means that unlike normal <script>, which only executes once when the
component is first imported, code inside <script setup> will execute every time
an instance of the component is created.

From: https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
 */


// This starter template is using Vue 3 <script setup> SFCs
// Check out
import HelloWorld from './components/HelloWorld.vue'
import PageHeader from './components/PageHeader.vue'
const user = {
  id: 10,
  name: "Fernando Constantino",
  avatarUrl: "https://instagram.fmii6-1.fna.fbcdn.net/v/t51.2885-19/s150x150/160833942_766379700979973_7163175520197855836_n.jpg?_nc_ht=instagram.fmii6-1.fna.fbcdn.net&_nc_ohc=fEavI8VlF1sAX8OJn2t&edm=ABfd0MgBAAAA&ccb=7-4&oh=cc6930e6e9d4486ed9609b448563d1a7&oe=61674082&_nc_sid=7bff83",
}
</script>

<template>
  <PageHeader/>
  <img
    alt="Vue logo"
    src="./assets/logo.png"
  />
  <HelloWorld msg="Hello Vue 3 + Vite" />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
