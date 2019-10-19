<template>
  <div id="image-viewer">
    <img v-if="inputSeen" alt="Input" :src="inputFilePath" />
    <img v-if="outputFileURL" alt="Output" :src="outputFileURL" />
    <img v-if="logoSeen" alt="Logo" src="../assets/logo.jpg" />
  </div>
</template>

<script>
export default {
  name: 'ImageViewer',
  props: ['inputFile', 'outputFileURL'],
  data: function() {
    return {
      inputFilePath: null
    }
  },
  watch: {
    inputFile: function(val) {
      this.inputFilePath = null
      if (val instanceof File) {
        const reader = new FileReader()
        reader.onload = e => {
          this.inputFilePath = e.target.result
        }
        reader.readAsDataURL(val)
      }
    }
  },
  computed: {
    logoSeen: function() {
      return this.inputFilePath ? false : true
    },
    inputSeen: function() {
      return !this.inputFilePath || this.outputFileURL ? false : true
    }
  }
}
</script>

<style scoped>
img {
  max-width: 100%;
  max-height: 40%;
}
</style>
