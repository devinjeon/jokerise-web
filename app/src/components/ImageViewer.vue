<template>
  <div id="image-viewer">
    <img alt="Image" :src="imgSrc" />
  </div>
</template>

<script>
export default {
  name: 'ImageViewer',
  props: ['src'],
  computed: {
    imgSrc: function() {
      if (typeof this.src == 'string' && this.src != '') {
        return this.src
      } else {
        return require('../assets/sample.jpg')
      }
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
