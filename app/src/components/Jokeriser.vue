<template>
  <div id="jokeriser">
    <div id="image-selector">
      <b-form-file
        v-model="inputFile"
        :state="Boolean(inputFile)"
        placeholder="Choose your face photo"
        accept=".jpg, .png"
        drop-placeholder="Drop file here..."
      ></b-form-file>
    </div>
    <div id="jokerise-button">
      <b-button
        block
        size="lg"
        v-if="canJokerise"
        :class="{ disabled: !canJokerise }"
        v-on:click="jokeriseImage"
      >
        Jokerise!
      </b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Jokeriser',
  data() {
    return {
      oldInputFile: null,
      inputFile: null,
      outputFileURL: null
    }
  },
  methods: {
    jokeriseImage: function() {
      if (this.inputFile instanceof File) {
        this.oldInputFile = this.inputFile
        // mock
        this.outputFileURL =
          'https://raw.githubusercontent.com/junkwhinger/jokerise/master/translated_samples/joaquin2.jpg'
        alert(this.inputFile.type)
      } else {
        alert('Invalid File')
      }
    }
  },
  watch: {
    inputFile: function(val) {
      if (val == null) {
        this.outputFileURL = null
      }
    }
  },
  computed: {
    canJokerise: function() {
      return this.oldInputFile != this.inputFile && this.inputFile
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#image-selector {
  text-align: left;
}
#jokeriser {
  text-align: center;
}
#jokerise-button {
  margin-top: 20px;
  margin-left: auto;
  margin-right: auto;
  width: 80%;
}
</style>
