<template>
  <div id="Layout">
    <top></top>
      <app-main></app-main>
    <!-- <bottom class="bottom"></bottom> -->
  </div>
</template>

<script>
import Top from '@/views/layout/components/Top'
// import Bottom from '@/views/layout/components/Bottom'
import AppMain from '@/views/layout/components/AppMain'

export default {
  name: 'Layout',
  components: {
    Top,
    // Bottom,
    AppMain
  }
}
</script>

<style>
html,
body {
  height: 100%;
  width: 100%;
  overflow-x: hidden
}
#Layout .top {
  margin-bottom: 46px
}
</style>
