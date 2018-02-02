<!--用于填写政策咨询,初版仅支持看自己的 -->
<template>
  <div id ='PolicyQa'>
    <group title="咨询人信息">
      <cell title="姓名" value="value">
        <x-input v-model="policyQaform.fullname"></x-input>
      </cell>
      <cell title="性别" value="value">
        <checker v-model="policyQaform.sex" default-item-class="sex-item" selected-item-class="sex-item-selected">
          <checker-item value="1">男</checker-item>
          <checker-item value="2">女</checker-item>
        </checker>
      </cell>
      <cell title="年龄" value="value">
        <x-input v-model="policyQaform.age"></x-input>
      </cell>
      <cell title="居住区域" value="value">
        <x-input v-model="policyQaform.livearea"></x-input>
      </cell>
      <cell title="联系方式" value="value">
        <x-input v-model="policyQaform.cellphone" :max="11"></x-input>
      </cell>
      <cell title="职业" value="value">
        <x-input v-model="policyQaform.occupation"></x-input>
      </cell>
      <cell title="婚姻状况" value="value">
        <x-input v-model="policyQaform.marriage"></x-input>
      </cell>
    </group>
    <group title="咨询内容">
      <cell title="标题" value="value">
        <x-input v-model="policyQaform.title"></x-input>
      </cell>
      <cell title="类型" value="value">
        <x-input v-model="policyQaform.type"></x-input>
      </cell>
      <cell title="内容" value="value">
        <x-textarea v-model="policyQaform.content" height="100" placeholder="咨询内容"></x-textarea>
      </cell>
      <cell title="线上/线下" value="value">
        <checker v-model="policyQaform.o2o" default-item-class="o2o-item" selected-item-class="o2o-item-selected">
          <checker-item value="1">线上</checker-item>
          <checker-item value="2">线下</checker-item>
        </checker>
      </cell>
    </group>
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleCommitpolicyqaform">提交</x-button>
    </group>
  </div>
</template>

<script>
import { Group, Cell, XInput, XTextarea, Checker, CheckerItem, XButton } from 'vux'
import { commitPolicyqaform } from '@/api/policy'

export default {
  name: 'policyQa',
  components: { Group, Cell, XInput, XTextarea, Checker, CheckerItem, XButton },
  data() {
    return {
      policyQaform: {
        fullname: '',
        sex: '',
        age: '',
        livearea: '',
        cellphone: '',
        occupation: '',
        marriage: '',
        title: '',
        type: '',
        content: '',
        o2o: ''
      }
    }
  },
  methods: {
    handleCommitpolicyqaform() {
      // console.log(this.sex) // vue获取的是标签的value
      // console.log(this.o2o)
      const qa_fullname = this.policyQaform.fullname
      const qa_sex = this.policyQaform.sex
      const qa_age = this.policyQaform.age
      const qa_live_area = this.policyQaform.livearea
      const qa_cellphone = this.policyQaform.cellphone
      const qa_occupation = this.policyQaform.occupation
      const qa_marriage = this.policyQaform.marriage
      const qa_title = this.policyQaform.title
      const qa_type = this.policyQaform.type
      const qa_content = this.policyQaform.content
      const qa_o2o = this.policyQaform.o2o
      const qa_user = this.$store.getters.username
      commitPolicyqaform(
        qa_user,
        qa_fullname,
        qa_sex,
        qa_age,
        qa_live_area,
        qa_cellphone,
        qa_occupation,
        qa_marriage,
        qa_title,
        qa_type,
        qa_content,
        qa_o2o
      ).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
        this.$router.push({ path: '/' })
      }).catch(error => {
        console.log(error)
        // reject(error)
      })
    }
  }
}
</script>

<style scoped>
.sex-item {
  width: 100px;
  height: 26px;
  line-height: 26px;
  text-align: center;
  border-radius: 3px;
  border: 1px solid #ccc;
  background-color: #fff;
  margin-right: 6px;
}
.sex-item-selected {
  background: #ffffff url(../../assets/active.png) no-repeat right bottom;
  border-color: #ff4a00;
}
.o2o-item {
  width: 100px;
  height: 26px;
  line-height: 26px;
  text-align: center;
  border-radius: 3px;
  border: 1px solid #ccc;
  background-color: #fff;
  margin-right: 6px;
}
.o2o-item-selected {
  background: #ffffff url(../../assets/active.png) no-repeat right bottom;
  border-color: #ff4a00;
}
</style>