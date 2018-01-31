<template>
  <div id="Init">
    <top class="top"></top>
      <transition>
        <router-view></router-view>
      </transition>
    <bottom></bottom>
  </div>
</template>

<script>
  import Top from './top.vue'
  import Bottom from './bottom.vue'
  export default {
    name: 'init',
    components: { Top, Bottom }
  }
</script>

<style>
  html, body {
    height: 100%;
    width: 100%;
    overflow-x: hidden;
  }
  #Init .top{margin-bottom: 46px;}
</style>
