<!--用于填写专业咨询问题及信息 -->
<template>
  <div id ='ProAdv'>
    <group title="咨询信息">
      <cell title="标题" value="value">
        <x-input v-model="proAdvform.title"></x-input>
      </cell>
      <cell title="类型" value="value">
        <x-input v-model="proAdvform.type"></x-input>
      </cell>
      <cell title="内容" value="value">
        <x-textarea v-model="proAdvform.content" height="100" placeholder="咨询内容"></x-textarea>
      </cell>
    </group>
    <group title="基本信息">
      <cell title="姓名" value="value">
        <x-input v-model="proAdvform.fullname"></x-input>
      </cell>
      <cell title="性别" value="value">
        <checker v-model="proAdvform.sex" default-item-class="sex-item" selected-item-class="sex-item-selected">
          <checker-item value="1">男</checker-item>
          <checker-item value="2">女</checker-item>
        </checker>
      </cell>
      <cell title="年龄" value="value">
        <x-input v-model="proAdvform.age"></x-input>
      </cell>
      <cell title="户籍所在地" value="value">
        <x-input v-model="proAdvform.household"></x-input>
      </cell>
      <cell title="身份证明" value="value">
        <x-input v-model="proAdvform.idnum" :max="11"></x-input>
      </cell>
      <cell title="民族" value="value">
        <x-input v-model="proAdvform.ethnic"></x-input>
      </cell>
      <cell title="政治面貌" value="value">
        <x-input v-model="proAdvform.political"></x-input>
      </cell>
      <cell title="宗教" value="value">
        <x-input v-model="proAdvform.religion"></x-input>
      </cell>
      <cell title="职业" value="value">
        <x-input v-model="proAdvform.occupation"></x-input>
      </cell>
      <cell title="就读年级" value="value">
        <x-input v-model="proAdvform.studygrade"></x-input>
      </cell>
      <cell title="文化程度" value="value">
        <x-input v-model="proAdvform.degree"></x-input>
      </cell>
      <cell title="所在社区" value="value">
        <x-input v-model="proAdvform.community"></x-input>
      </cell>
      <cell title="联系方式" value="value">
        <x-input v-model="proAdvform.contact"></x-input>
      </cell>
      <cell title="家庭住址" value="value">
        <x-input v-model="proAdvform.liveaddress"></x-input>
      </cell>
      <cell title="婚姻状况" value="value">
        <x-input v-model="proAdvform.marriage"></x-input>
      </cell>
    </group>
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleCommitroadvform">提交</x-button>
    </group>
  </div>
</template>

<script>
import { Group, Cell, XInput, XTextarea, Checker, CheckerItem, XButton } from 'vux'
import { commitProadvform } from '@/api/proadv'

export default {
  name: 'ProAdv',
  components: { Group, Cell, XInput, XTextarea, Checker, CheckerItem, XButton },
  data() {
    return {
      proAdvform: {
        title: '',
        type: '',
        content: '',
        fullname: '',
        sex: '',
        age: '',
        household: '',
        idnum: '',
        ethnic: '',
        political: '',
        religion: '',
        occupation: '',
        studygrade: '',
        degree: '',
        community: '',
        contact: '',
        liveaddress: '',
        marriage: ''
      }
    }
  },
  methods: {
    handleCommitroadvform() {
      // console.log(this.sex) // vue获取的是标签的value
      // console.log(this.o2o)
      const proadv_question_title = this.proAdvform.title
      const proadv_question_type = this.proAdvform.type
      const proadv_question_content = this.proAdvform.content
      const proadv_full_name = this.proAdvform.fullname
      const proadv_sex = this.proAdvform.sex
      const proadv_age = this.proAdvform.age
      const proadv_house_hold = this.proAdvform.household
      const proadv_id_num = this.proAdvform.idnum
      const proadv_ethnic = this.proAdvform.ethnic
      const proadv_political_status = this.proAdvform.political
      const proadv_religion = this.proAdvform.religion
      const proadv_occupation = this.proAdvform.occupation
      const proadv_studying_grade = this.proAdvform.studygrade
      const proadv_degree_of_education = this.proAdvform.degree
      const proadv_community = this.proAdvform.community
      const proadv_contact = this.proAdvform.contact
      const proadv_live_address = this.proAdvform.liveaddress
      const proadv_marriage = this.proAdvform.marriage
      const proadv_user = this.$store.getters.username
      commitProadvform(
        proadv_user,
        proadv_question_title,
        proadv_question_type,
        proadv_question_content,
        proadv_full_name,
        proadv_sex,
        proadv_age,
        proadv_house_hold,
        proadv_id_num,
        proadv_ethnic,
        proadv_political_status,
        proadv_religion,
        proadv_occupation,
        proadv_studying_grade,
        proadv_degree_of_education,
        proadv_community,
        proadv_contact,
        proadv_live_address,
        proadv_marriage
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
  background: #ffffff url(../../../assets/active.png) no-repeat right bottom;
  border-color: #ff4a00;
}
</style>