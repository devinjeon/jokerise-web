<template>
  <div class="container-fluid d-flex justify-content-center">
    <div id="app">
      <h1>Why so serious?</h1>
      <p>
        Not sure if Joker face would look good on you for Halloween? Try
        <b>Jokerise</b>!
      </p>
      <p>
        <a href="https://github.com/junkwhinger/jokerise">Source code</a> made
        by <a href="https://jsideas.net">Junsik Hwang</a>,
        <a href="https://hyojun.me">Hyojun Jeon</a>
      </p>
      <Jokerise />
      <p>
        NOTE: Your original photo is not saved on the server and the jokerised
        image will be deleted after 24 hours.
      </p>
    </div>
  </div>
</template>

<script>
import Jokerise from './components/Jokerise.vue'

export default {
  name: 'app',
  components: {
    Jokerise
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
  margin-bottom: 100px;
  width: 70%;
  text-align: center;
}
h1 {
  margin-bottom: 20px;
}
a {
  color: #555555;
}
</style>
