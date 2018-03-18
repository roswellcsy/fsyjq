<!--用于填写登记志愿者信息 -->
<template>
  <div id ='VolunteerRegister'>
    <!-- <group title="基本用户信息">
      <cell title="姓名" value="value">
        <x-input v-model="userinfo.name"></x-input>
      </cell>
      <cell title="性别" value="value">
        <x-input v-model="userinfo.sex"></x-input>
      </cell>
      <cell title="联系电话" value="value"></cell>
        <x-input v-model="userinfo.cellphone"></x-input>
      <cell title="电邮" value="value"></cell>
        <x-input v-model="userinfo.email"></x-input>
    </group> -->
    <group>
      <cell title="籍贯" value="value">
        <x-input v-model="volinfo.jiguan" placeholder="选填"></x-input>
      </cell>
      <cell title="住址" value="value">
        <x-input v-model="volinfo.liveaddress" placeholder="选填"></x-input>
      </cell>
      <cell title="婚姻状况" value="value">
        <x-input v-model="volinfo.marriage" placeholder="必填"></x-input>
      </cell>
      <cell title="证件类型" value="value">
        <x-input v-model="volinfo.idcardtype" placeholder="必填"></x-input>
      </cell>
      <cell title="证件号码" value="value">
        <x-input v-model="volinfo.idnum" placeholder="选填"></x-input>
      </cell>
      <cell title="出生日期（年月日）" value="value">
        <x-input v-model="volinfo.birthday" placeholder="选填"></x-input>
      </cell>
      <cell title="毕业院校" value="value">
        <x-input v-model="volinfo.graduateschool" placeholder="选填"></x-input>
      </cell>
      <cell title="毕业时间" value="value">
        <x-input v-model="volinfo.graduatedate" placeholder="选填"></x-input>
      </cell>
      <cell title="学历" value="value">
        <x-input v-model="volinfo.education" placeholder="选填"></x-input>
      </cell>
      <cell title="专业" value="value">
        <x-input v-model="volinfo.profession" placeholder="选填"></x-input>
      </cell>
      <cell title="工作单位" value="value">
        <x-input v-model="volinfo.employer" placeholder="选填"></x-input>
      </cell>
      <cell title="职务" value="value">
        <x-input v-model="volinfo.position" placeholder="选填"></x-input>
      </cell>
      <cell title="通讯地址" value="value">
        <x-input v-model="volinfo.mailaddress" placeholder="选填"></x-input>
      </cell>
      <cell title="邮编" value="value">
        <x-input v-model="volinfo.zipcode" placeholder="选填"></x-input>
      </cell>
      <cell title="固定电话" value="value">
        <x-input v-model="volinfo.contact" placeholder="选填"></x-input>
      </cell>
      <cell title="志愿服务时间" value="value">
        <x-input v-model="volinfo.servicedate" placeholder="必填"></x-input>
      </cell>
      <cell title="志愿服务区" value="value">
        <x-input v-model="volinfo.servicearea" placeholder="选填"></x-input>
      </cell>
      <cell title="技能" value="value">
        <x-textarea v-model="volinfo.skills" placeholder="选填"></x-textarea>
      </cell>
    </group>
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleCommitvolregister">提交</x-button>
    </group>
  </div>
</template>

<script>
import { Group, Cell, XInput, XButton, XTextarea } from 'vux'
import { commitvolregisterform } from '@/api/volunteer'
export default {
  name: 'volunteerRegister',
  components: { Group, Cell, XInput, XButton, XTextarea },
  data() {
    return {
      volinfo: {
        jiguan: '',
        liveaddress: '',
        marriage: '',
        idcardtype: '',
        idnum: '',
        birthday: '1990-01-01',
        graduateschool: '',
        graduatedate: '1990-01-01',
        education: '',
        profession: '',
        employer: '',
        position: '',
        mailaddress: '',
        zipcode: '',
        contact: '',
        servicedate: '',
        servicearea: '',
        skills: ''
      }
    }
  },
  methods: {
    handleCommitvolregister() {
      const volinfo_jiguan = this.volinfo.jiguan
      const volinfo_live_address = this.volinfo.liveaddress
      const volinfo_marriage = this.volinfo.marriage
      const volinfo_idcard_type = this.volinfo.idcardtype
      const volinfo_id_num = this.volinfo.idnum
      const volinfo_birthday = this.volinfo.birthday
      const volinfo_graduate_school = this.volinfo.graduateschool
      const volinfo_graduate_date = this.volinfo.graduatedate
      const volinfo_education = this.volinfo.education
      const volinfo_profession = this.volinfo.profession
      const volinfo_employer = this.volinfo.employer
      const volinfo_position = this.volinfo.position
      const volinfo_mail_address = this.volinfo.mailaddress
      const volinfo_zipcode = this.volinfo.zipcode
      const volinfo_contact_number = this.volinfo.contact
      const volinfo_service_area = this.volinfo.servicearea
      const volinfo_service_date = this.volinfo.servicedate
      const volinfo_skills = this.volinfo.skills
      const volinfo_user_id = window.localStorage.getItem('user_id')
      commitvolregisterform(
        volinfo_user_id,
        volinfo_jiguan,
        volinfo_live_address,
        volinfo_marriage,
        volinfo_idcard_type,
        volinfo_id_num,
        volinfo_birthday,
        volinfo_graduate_school,
        volinfo_graduate_date,
        volinfo_education,
        volinfo_profession,
        volinfo_employer,
        volinfo_position,
        volinfo_mail_address,
        volinfo_zipcode,
        volinfo_contact_number,
        volinfo_service_area,
        volinfo_service_date,
        volinfo_skills
      ).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
        this.$router.push({ path: '/personal/userInfo' })
      }).catch(error => {
        console.log(error)
        // reject(error)
      })
    }
  }
}

</script>

<style>

</style>