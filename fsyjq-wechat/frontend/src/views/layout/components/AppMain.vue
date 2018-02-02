<template>
  <!-- <section class="app-main"> -->
    <transition name="fade" mode="out-in">
      <!-- <router-view :key="key"></router-view> -->
      <div id = "AppMain">
        <router-view></router-view>
      </div>
    </transition>
  <!-- </section> -->
</template>

<script>
export default {
  name: 'AppMain',
  computed: {
    // key() {
    //   return this.$route.name !== undefined ? this.$route.name + +new Date() : this.$route + +new Date()
    // }
  }
}
</script>

<style scoped>
#AppMain {
  margin-bottom: 57px;
}
</style>

