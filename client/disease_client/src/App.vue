<template>
  <CovidData msg="Welcome to Your Vue.js App"/>
</template>

<script>
import CovidData from './components/CovidData.vue';
import '@coreui/coreui/dist/css/coreui.min.css';

export default {
  name: 'App',
  components: {
    CovidData
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
