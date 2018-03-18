<!--用于展示我的专业咨询详细内容 -->

<template>
  <div id ='MyProAdv'>
    <!-- <group> -->
    <!-- 根据后端获取到的发布活动列表，动态生成公益活动清单 -->
    <group>
      <cell title='咨询主题:' :value=content[0].proadv_question_title></cell>
      <cell title='咨询内容:' :value=content[0].proadv_question_content></cell>
      <cell title='咨询类型:' :value=content[0].proadv_question_type></cell>
      <cell title='服务内容:' :value=content[0].proadv_serv_content></cell>      
      <datetime title='服务时间:' :value=content[0].proadv_serv_date :readonly=True></datetime>
    </group>
  </div>
</template>

<script>
import { getMyProAdv } from '@/api/proadv'
import { Group, Cell, FormPreview, Datetime } from 'vux'
// import { METHODS } from 'http';
export default {
  name: 'mypolicyqa',
  components: { Group, Cell, FormPreview, Datetime },
  data() { // data()需要跟return
    return {
      content: this.content
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      getMyProAdv(window.localStorage.getItem('clicktitle')).then(response => {
        this.content = response
        // window.localStorage.setItem('policyqalists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>