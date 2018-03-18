<!--用于展示志愿者能力培训清单 -->

<template>
  <div id ='TrainingList'>
    <!-- <group> -->
    <!-- 根据后端获取到的发布活动列表，动态生成公益活动清单 -->
    <group>
      <template v-for="list in lists">
          <cell :title=list.at_theme :value=list.at_date @click.native.prevent="setCurrenttitle($event)" link="/volServ/trainingDetail"></cell>
      </template>
    </group>
  </div>
</template>

<script>
import { fetchTraininglist } from '@/api/volunteer'
import { Group, Cell } from 'vux'
// import { METHODS } from 'http';
export default {
  name: 'trainingList',
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
      fetchTraininglist().then(response => {
        this.lists = response
        window.localStorage.setItem('traininglists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
    },
    setCurrenttitle() {
      const el = event.currentTarget
      window.localStorage.setItem('clicktrainingtitle', el.innerText.split('\n')[0])
    }
  }
}
</script>

<style>

</style>