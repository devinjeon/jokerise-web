<template>
  <div class="container-fluid d-flex justify-content-center">
    <div id="app">
      <h1>Why so serious?</h1>
      <p>
        Not sure if Joker face would look good on you for Halloween? Try
        <b>Jokeriser</b>!
      </p>
      <Jokeriser />
    </div>
  </div>
</template>

<script>
import Jokeriser from './components/Jokeriser.vue'

export default {
  name: 'app',
  components: {
    Jokeriser
  }
}
</script>

<style>
body {
  background-color: black;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #999999;
  margin-top: 100px;
  width: 70%;
  text-align: center;
}
h1 {
  margin-bottom: 20px;
}
</style>
