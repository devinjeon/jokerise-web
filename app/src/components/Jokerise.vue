<template>
  <div id="jokeriser">
    <ImageViewer :src="src" />
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
      src: null
    }
  },
  methods: {
    jokeriseImage: function() {
      if (this.inputFile instanceof File) {
        this.oldInputFile = this.inputFile
        // mock
        let form = new FormData()
        form.append('file', this.inputFile)
        this.$axios
          .post('/jokerise', form, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then(response => {
            this.src =
              process.env.VUE_APP_API_BASE_URL + '/jokerise/' + response.data
            alert('Jokerised!')
          })
          .catch(error => {
            alert(error)
          })
      } else {
        alert('Invalid file')
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
