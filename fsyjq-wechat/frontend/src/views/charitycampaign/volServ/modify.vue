<!--用于填写登记志愿者信息 -->
<template>
  <div id ='VolunteerModify'>
    <group>
      <cell title="籍贯" value="value">
        <x-input v-model="volinfo.volinfo_jiguan"></x-input>
      </cell>
      <cell title="住址">
        <x-input v-model="volinfo.volinfo_live_address"></x-input>
      </cell>
      <cell title="婚姻状况" value="value">
        <x-input v-model="volinfo.volinfo_marriage"></x-input>
      </cell>
      <cell title="证件类型" value="value">
        <x-input v-model="volinfo.volinfo_idcard_type" required=True></x-input>
      </cell>
      <cell title="证件号码" value="value">
        <x-input v-model="volinfo.volinfo_id_num" required=True></x-input>
      </cell>
      <cell title="出生日期（年月日）" value="value">
        <x-input v-model="volinfo.volinfo_birthday"></x-input>
      </cell>
      <cell title="毕业院校" value="value">
        <x-input v-model="volinfo.volinfo_graduate_school"></x-input>
      </cell>
      <cell title="毕业时间" value="value">
        <x-input v-model="volinfo.volinfo_graduate_date"></x-input>
      </cell>
      <cell title="学历" value="value">
        <x-input v-model="volinfo.volinfo_education"></x-input>
      </cell>
      <cell title="专业" value="value">
        <x-input v-model="volinfo.volinfo_profession"></x-input>
      </cell>
      <cell title="工作单位" value="value">
        <x-input v-model="volinfo.volinfo_employer"></x-input>
      </cell>
      <cell title="职务" value="value">
        <x-input v-model="volinfo.volinfo_position"></x-input>
      </cell>
      <cell title="通讯地址" value="value">
        <x-input v-model="volinfo.volinfo_mail_address"></x-input>
      </cell>
      <cell title="邮编" value="value">
        <x-input v-model="volinfo.volinfo_zipcode"></x-input>
      </cell>
      <cell title="固定电话" value="value">
        <x-input v-model="volinfo.volinfo_contact_number"></x-input>
      </cell>
      <cell title="志愿服务时间" value="value">
        <x-input v-model="volinfo.volinfo_service_date" required=True></x-input>
      </cell>
      <cell title="志愿服务区" value="value">
        <x-input v-model="volinfo.volinfo_service_area"></x-input>
      </cell>
      <cell title="技能" value="value">
        <x-textarea v-model="volinfo.volinfo_skills"></x-textarea>
      </cell>
    </group>
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleCommitvolmodify">提交</x-button>
    </group>
  </div>
</template>

<script>
import { Group, Cell, XInput, XButton, XTextarea } from 'vux'
import { commitvolmodifyform, getVolinfo } from '@/api/volunteer'
export default {
  name: 'volunteerModify',
  components: { Group, Cell, XInput, XButton, XTextarea },
  data() {
    return {
      // volinfo: {
      //   jiguan: '',
      //   liveaddress: '',
      //   marriage: '',
      //   idcardtype: '',
      //   idnum: '',
      //   birthday: '1990-01-01',
      //   graduateschool: '',
      //   graduatedate: '1990-01-01',
      //   education: '',
      //   profession: '',
      //   employer: '',
      //   position: '',
      //   mailaddress: '',
      //   zipcode: '',
      //   contact: '',
      //   servicedate: '',
      //   servicearea: '',
      //   skills: ''
      // },
      volinfo: this.volinfo
    }
  },
  created() {
    this.fetchData()
    // this.fetchImagelist()
  },
  methods: {
    fetchData() {
      getVolinfo(window.localStorage.getItem('username')).then(response => {
        this.volinfo = response[0]
        // window.localStorage.setItem('campaignlists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
    },
    handleCommitvolmodify() {
      const volinfo_jiguan = this.volinfo.volinfo_jiguan
      const volinfo_live_address = this.volinfo.volinfo_live_address
      const volinfo_marriage = this.volinfo.volinfo_marriage
      const volinfo_idcard_type = this.volinfo.volinfo_idcard_type
      const volinfo_id_num = this.volinfo.volinfo_id_num
      const volinfo_birthday = this.volinfo.volinfo_birthday
      const volinfo_graduate_school = this.volinfo.volinfo_graduate_school
      const volinfo_graduate_date = this.volinfo.volinfo_graduate_date
      const volinfo_education = this.volinfo.volinfo_education
      const volinfo_profession = this.volinfo.volinfo_profession
      const volinfo_employer = this.volinfo.volinfo_employer
      const volinfo_position = this.volinfo.volinfo_position
      const volinfo_mail_address = this.volinfo.volinfo_mail_address
      const volinfo_zipcode = this.volinfo.volinfo_zipcode
      const volinfo_contact_number = this.volinfo.volinfo_contact_number
      const volinfo_service_area = this.volinfo.volinfo_service_area
      const volinfo_service_date = this.volinfo.volinfo_service_date
      const volinfo_skills = this.volinfo.volinfo_skills
      const vol_info_id = window.localStorage.getItem('vol_info_id')
      const volinfo_user_id = window.localStorage.getItem('user_id')
      commitvolmodifyform(
        vol_info_id,
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