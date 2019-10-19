<template>
  <div id="app">
    <img alt="Example" src="./assets/logo.jpg" width="80%" />
    <jokeriser />
  </div>
</template>

<script>
import jokeriser from './components/Jokeriser.vue'

export default {
  name: 'app',
  components: {
    jokeriser
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #999999;
  margin-top: 60px;
}
</style>
