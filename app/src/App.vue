<template>
  <div class="container-fluid d-flex justify-content-center">
    <div id="app">
      <h1>Why so serious?</h1>
      <p>
        Not sure if Joker face would look good on you for Halloween? Try
        <b>Jokerise</b>!
      </p>
      <Jokerise />
      <section>
        <p>
          NOTE: All the photos uploaded are not saved on the server and the
          jokerised images will be deleted after 24 hours.
        </p>
        <p>
          * Source Codes:
          <a
            href="https://github.com/junkwhinger/jokerise"
            v-on:click="gaVisitEvent('sourcecode:jokerise')"
            >Jokerise</a
          >
          /
          <a
            href="https://github.com/devinjeon/jokerise-web"
            v-on:click="gaVisitEvent('sourcecode:jokerise-web')"
            >Web</a
          >
          made by
          <a href="https://jsideas.net" v-on:click="gaVisitEvent('jsideas.net')"
            >Junsik Hwang</a
          >,
          <a href="https://hyojun.me" v-on:click="gaVisitEvent('hyojun.me')"
            >Hyojun Jeon</a
          >
        </p>
      </section>
    </div>
  </div>
</template>

<script>
import Jokerise from './components/Jokerise.vue'

export default {
  name: 'app',
  components: {
    Jokerise
  },
  mounted() {
    this.$ga.page('/main')
  },
  methods: {
    gaVisitEvent: function(label) {
      this.$ga.event('etc', 'visit', label, 1)
    }
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
