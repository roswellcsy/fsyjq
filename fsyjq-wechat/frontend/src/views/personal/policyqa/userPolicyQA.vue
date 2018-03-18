<!--用于展示我的政策咨询详细内容 -->

<template>
  <div id ='MyPolicyQA'>
    <!-- <group> -->
    <!-- 根据后端获取到的发布活动列表，动态生成公益活动清单 -->
    <group>
      <cell title='咨询主题:' :value=content[0].qa_title></cell>
      <cell title='咨询内容:' :value=content[0].qa_content></cell>
      <cell title='咨询类型:' :value=content[0].qa_type></cell>
      <datetime title='咨询时间:' :value=content[0].qa_ask_date :readonly=True></datetime>
      <cell title='回答内容:' :value=content[0].qa_answer></cell>
      <datetime title='回答时间:' :value=content[0].qa_answer_date :readonly=True></datetime>
    </group>
  </div>
</template>

<script>
import { getMyPolicyQA } from '@/api/policy'
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
      getMyPolicyQA(window.localStorage.getItem('clicktitle')).then(response => {
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