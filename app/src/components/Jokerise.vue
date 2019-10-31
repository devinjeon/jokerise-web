<template>
  <div id="jokeriser">
    <ImageViewer :src="src" v-show="!isLoading" />
    <div id="spinner" v-show="isLoading">
      <b-spinner label="Loading..."></b-spinner>
    </div>
    <div id="image-selector">
      <b-form-file
        v-model="inputFile"
        :state="Boolean(inputFile)"
        placeholder="Choose your photo"
        accept=".jpg, .jpeg, .png"
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
import ImageViewer from './ImageViewer.vue'

export default {
  name: 'Jokerise',
  components: {
    ImageViewer
  },
  data() {
    return {
      oldInputFile: null,
      inputFile: null,
      src: null,
      isLoading: false
    }
  },
  methods: {
    jokeriseImage: function() {
      this.$ga.event('jokerise', 'try', '-', 1)

      if (this.inputFile instanceof File) {
        this.oldInputFile = this.inputFile
        // mock
        let form = new FormData()
        form.append('file', this.inputFile)
        this.isLoading = true

        this.$ga.event('jokerise', 'try:upload', '-', 2)
        this.$axios
          .post('/jokerise', form, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then(response => {
            this.isLoading = false
            this.src = response.data
            alert('Jokerised!')

            this.$ga.event('jokerise', 'jokerised', '-', 3)
          })
          .catch(error => {
            this.isLoading = false
            alert(error)
            this.$ga.event('jokerise', 'error', error, 3)
          })
      } else {
        alert('Invalid file')
        this.$ga.event('jokerise', 'error', 'invalid_file', 2)
      }
    }
  },
  watch: {
    inputFile: function(val) {
      if (val != this.oldInputFile && val instanceof File) {
        const reader = new FileReader()
        reader.onload = e => {
          this.src = e.target.result
        }
        reader.readAsDataURL(val)
      } else if (val == null) {
        this.src = null
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
  margin-left: auto;
  margin-right: auto;
  max-width: 600px;
  width: 100%;
}
#spinner {
  margin-left: auto;
  margin-right: auto;
  margin-top: 100px;
  margin-bottom: 100px;
  width: 100%;
}
#jokeriser {
  text-align: center;
}
#jokerise-button {
  margin-top: 20px;
  margin-left: auto;
  margin-right: auto;
  width: 80%;
  max-width: 300px;
}
</style>
