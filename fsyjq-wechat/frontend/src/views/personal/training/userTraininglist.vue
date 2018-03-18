<!--用于展示我的公益活动清单 -->

<template>
  <div id ='MyTrainingList'>
    <!-- <group> -->
    <!-- 根据后端获取到的发布活动列表，动态生成公益活动清单 -->
    <group>
      <template v-for="list in lists">
          <cell :title=list.at_theme :value=list.at_date @click.native.prevent="setCurrenttitle($event)" link="/personal/userTraining"></cell>
      </template>
    </group>
  </div>
</template>

<script>
import { fetchMyTraininglist } from '@/api/volunteer'
import { Group, Cell, FormPreview } from 'vux'
// import { METHODS } from 'http';
export default {
  name: 'mytraininglist',
  components: { Group, Cell, FormPreview },
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
      fetchMyTraininglist(window.localStorage.getItem('username')).then(response => {
        this.lists = response
        window.localStorage.setItem('mytraininglists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
    },
    setCurrenttitle() {
      const el = event.currentTarget
      window.localStorage.setItem('clickmytrainingtitle', el.innerText.split('\n')[0])
    }
  }
}
</script>

<style>

</style>