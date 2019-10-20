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
#image-viewer {
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}
img {
  max-height: 500px;
  max-width: 100%;
  width: auto;
}
</style>
