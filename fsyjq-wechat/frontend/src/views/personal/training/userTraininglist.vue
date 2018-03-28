<!--用于展示我的公益活动清单 -->

<template>
  <div id ='MyTrainingList'>
    <!-- <group> -->
    <!-- 根据后端获取到的发布活动列表，动态生成公益活动清单 -->
    <template v-if="vol_info_id !== null">
      <group>
        <template v-for="list in lists">
            <cell :title=list.at_theme :value=list.at_date @click.native.prevent="setCurrenttitle($event)" link="/personal/userTraining"></cell>
        </template>
      </group>
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" link="/volServ/traningList">能力培训清单</x-button>
      </group>
    </template>
    <template v-else-if="vol_info_id === null">
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" link="/volServ/register">请先登记成为志愿者</x-button>
      </group>
    </template>
  </div>
</template>

<script>
import { fetchMyTraininglist } from '@/api/volunteer'
import { Group, Cell, FormPreview, XButton } from 'vux'
// import { METHODS } from 'http';
export default {
  name: 'mytraininglist',
  components: { Group, Cell, FormPreview, XButton },
  data() { // data()需要跟return
    return {
      lists: this.lists,
      vol_info_id: window.localStorage.getItem('vol_info_id')
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