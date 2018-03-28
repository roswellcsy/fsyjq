<!--用于展示我的专业咨询清单 -->

<template>
  <div id ='MyProAdvList'>
    <!-- <group> -->
    <!-- 根据后端获取到的发布活动列表，动态生成公益活动清单 -->
    <group>
      <template v-for="list in lists">
          <cell :title=list.proadv_question_title :value=list.proadv_status @click.native.prevent="setCurrenttitle($event)" link="/personal/userProAdv"></cell>
      </template>
    </group>
    <template>
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" link="/proAdv/index">新增专业咨询</x-button>
      </group>
    </template>
  </div>
</template>

<script>
import { getMyProAdvlist } from '@/api/proadv'
import { Group, Cell, FormPreview, XButton } from 'vux'
// import { METHODS } from 'http';
export default {
  name: 'myproadvlist',
  components: { Group, Cell, FormPreview, XButton },
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
      getMyProAdvlist(window.localStorage.getItem('username')).then(response => {
        this.lists = response
        window.localStorage.setItem('proadvlists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
    },
    setCurrenttitle() {
      const el = event.currentTarget
      window.localStorage.setItem('clicktitle', el.innerText.split('\n')[0])
    }
  }
}
</script>

<style>

</style>