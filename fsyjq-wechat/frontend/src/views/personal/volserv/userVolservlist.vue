<!--用于展示我报名的公益活动清单 -->

<template>
  <div id ='myVolservList'>
    <!-- <group> -->
    <!-- 根据后端获取到的发布活动列表，动态生成公益活动清单 -->
    <group>
      <template v-for="list in lists">
          <cell :title=list.campaign_name :value=list.campaign_date @click.native.prevent="setCurrenttitle($event)" link="/personal/userVolServ"></cell>
      </template>
    </group>
  </div>
</template>

<script>
import { fetchMylist } from '@/api/volunteer'
import { Group, Cell } from 'vux'
// import { METHODS } from 'http';
export default {
  name: 'myvolservlist',
  components: { Group, Cell },
  data() { // data()需要跟return
    return {
      lists: this.lists
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      fetchMylist().then(response => {
        this.lists = response
        window.localStorage.setItem('myvolservlists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
    },
    setCurrenttitle() {
      const el = event.currentTarget
      window.localStorage.setItem('clickmyvolservtitle', el.innerText.split('\n')[0])
    }
  }
}
</script>

<style>

</style>