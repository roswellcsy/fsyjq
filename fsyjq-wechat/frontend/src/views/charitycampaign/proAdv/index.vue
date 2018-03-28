<!--用于填写专业咨询问题及信息 -->
<template>
  <div id ='ProAdv'>
    <group title="咨询信息">
      <cell title="标题" value="value">
        <x-input v-model="proAdvform.title" placeholder="必填" required></x-input>
      </cell>
      <!-- <cell title="类型" value="value">
        <x-input v-model="proAdvform.type"></x-input>
      </cell> -->
      <selector title="类型" placeholder="必选" v-model="proAdvform.type" :options="questiontypeOption" @on-change="onChange" direction></selector>
      <cell title="内容" value="value" placeholder="必填">
        <x-textarea v-model="proAdvform.content" height="100" placeholder="必填咨询内容"></x-textarea>
      </cell>
    </group>
    <group title="基本信息">
      <cell title="姓名" value="value">
        <x-input v-model="proAdvform.fullname" placeholder="必填"></x-input>
      </cell>
      <!-- <cell title="性别" value="value">
        <checker v-model="proAdvform.sex" default-item-class="sex-item" selected-item-class="sex-item-selected">
          <checker-item value="1">男</checker-item>
          <checker-item value="2">女</checker-item>
        </checker>
      </cell> -->
      <selector placeholder="必选" title="性别" v-model="proAdvform.sex" :options="sexoption" @on-change="onChange"></selector>
      <cell title="年龄" value="value">
        <x-input v-model="proAdvform.age"  placeholder="必填数字"></x-input>
      </cell>
      <cell title="户籍所在地" value="value">
        <x-input v-model="proAdvform.household" placeholder="选填"></x-input>
      </cell>
      <cell title="身份证明" value="value">
        <x-input v-model="proAdvform.idnum" :max="11" placeholder="选填"></x-input>
      </cell>
      <!-- <cell title="民族" value="value">
        <x-input v-model="proAdvform.ethnic"></x-input>
      </cell> -->
      <selector title="民族" placeholder="可选" v-model="proAdvform.ethnic" :options="ethnicOption" @on-change="onChange" direction></selector>
      <!-- <cell title="政治面貌" value="value">
        <x-input v-model="proAdvform.political"></x-input>
      </cell> -->
      <selector title="政治面貌" placeholder="可选" v-model="proAdvform.political" :options="politicalOption" @on-change="onChange" direction></selector>
      <cell title="宗教" value="value">
        <x-input v-model="proAdvform.religion" placeholder="选填"></x-input>
      </cell>
      <cell title="职业" value="value">
        <x-input v-model="proAdvform.occupation" placeholder="选填"></x-input>
      </cell>
      <cell title="就读年级" value="value">
        <x-input v-model="proAdvform.studygrade" placeholder="选填"></x-input>
      </cell>
      <cell title="文化程度" value="value">
        <x-input v-model="proAdvform.degree" placeholder="选填"></x-input>
      </cell>
      <cell title="所在社区" value="value">
        <x-input v-model="proAdvform.community" placeholder="选填"></x-input>
      </cell>
      <cell title="联系方式" value="value">
        <x-input v-model="proAdvform.contact" placeholder="选填"></x-input>
      </cell>
      <cell title="家庭住址" value="value">
        <x-input v-model="proAdvform.liveaddress" placeholder="选填"></x-input>
      </cell>
      <!-- <cell title="婚姻状况" value="value">
        <x-input v-model="proAdvform.marriage" placeholder="选填"></x-input>
      </cell> -->
      <selector title="婚姻状况" placeholder="可选" v-model="proAdvform.marriage" :options="marriageOption" @on-change="onChange" direction></selector>
    </group>
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleCommitroadvform">提交</x-button>
    </group>
  </div>
</template>

<script>
import { Group, Cell, XInput, XTextarea, Checker, CheckerItem, XButton, Selector } from 'vux'
import { commitProadvform } from '@/api/proadv'

export default {
  name: 'ProAdv',
  components: { Group, Cell, XInput, XTextarea, Checker, CheckerItem, XButton, Selector },
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
      },
      sexoption: [{
        value: '男',
        key: '1'
      }, {
        value: '女',
        key: '2'
      }],
      questiontypeOption: [{
        key: '1',
        value: '亲子关系问题'
      }, {
        key: '2',
        value: '婚姻问题'
      }, {
        key: '3',
        value: '家庭纠纷'
      }, {
        key: '4',
        value: '经济问题'
      }, {
        key: '5',
        value: '职业问题'
      }, {
        key: '6',
        value: '住屋问题'
      }, {
        key: '7',
        value: '家庭暴力致伤/死(受害对象:子女/配偶/老人/其它'
      }, {
        key: '8',
        value: '个人精神/情绪问题'
      }, {
        key: '9',
        value: '个人行为问题(吸毒/酒/赌博)'
      }, {
        key: '10',
        value: '恋爱/交友问题'
      }, {
        key: '11',
        value: '患病/复康问题(病类)'
      }, {
        key: '12',
        value: '未婚怀孕'
      }, {
        key: '13',
        value: '收养'
      }, {
        key: '14',
        value: '其它'
      }],
      ethnicOption: [{
        key: '1',
        value: '汉族'
      }, {
        key: '2',
        value: '少数民族'
      }, {
        key: '3',
        value: '其他'
      }],
      politicalOption: [{
        key: '1',
        value: '中共党员'
      }, {
        key: '2',
        value: '民主党派成员'
      }, {
        key: '3',
        value: '共青团员'
      }, {
        key: '4',
        value: '群众'
      }, {
        key: '5',
        value: '其他'
      }],
      marriageOption: [{
        key: '1',
        value: '未婚'
      }, {
        key: '2',
        value: '已婚'
      }, {
        key: '3',
        value: '离异'
      }, {
        key: '4',
        value: '丧偶'
      }]
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
    },
    onChange(val) {
      // console.log(val)
      console.log(val)
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