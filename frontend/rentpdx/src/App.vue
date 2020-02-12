<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <dashboard msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import dashboard from "./components/dashboard.vue";

export default {
  name: "App",
  components: {
    dashboard
  }
};
</script>

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
