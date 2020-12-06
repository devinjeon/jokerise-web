<template>
  <div id="app">
    <h1>Why so serious?</h1>
    <Jokerise />
    <section>
      <p class="notice">
        NOTICE: Sorry, This Jokerise web service is closed now.
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
  margin-left: auto;
  margin-right: auto;
  width: 70%;
  text-align: center;
}
h1 {
  margin-bottom: 20px;
}
a {
  color: #555555;
}
p.notice {
  margin-top: 30px;
  color: red;
}
</style>
