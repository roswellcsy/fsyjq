<!--用于展示我的政策咨询清单 -->

<template>
  <div id ='MyPolicyQAList'>
    <!-- <group> -->
    <!-- 根据后端获取到的发布活动列表，动态生成公益活动清单 -->
    <group>
      <template v-for="list in lists">
          <cell :title=list.qa_title :value=list.qa_ask_date @click.native.prevent="setCurrenttitle($event)" link="/personal/userPolicyQA"></cell>
      </template>
    </group>
    <template>
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" link="/policy/policyQa">填写政策咨询</x-button>
      </group>
    </template>
  </div>
</template>

<script>
import { getMyPolicyQAlist } from '@/api/policy'
import { Group, Cell, FormPreview, XButton } from 'vux'
// import { METHODS } from 'http';
export default {
  name: 'mypolicyqalist',
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
      getMyPolicyQAlist(window.localStorage.getItem('username')).then(response => {
        this.lists = response
        window.localStorage.setItem('policyqalists', this.lists)
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