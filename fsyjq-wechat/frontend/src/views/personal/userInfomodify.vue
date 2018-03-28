<template>
    <div id="UserInfoModify">
      <group title="个人信息">
        <cell title="用户名" :value=userinfo.user_information_name>
          <x-input v-model="userinfo.user_information_name"></x-input>
        </cell>
        <!-- <cell title="性别" :value=userinfo.user_information_sex>
          <x-input v-model="userinfo.user_information_sex"></x-input>
        </cell> -->
        <!-- <template v-if="userinfo.sex==='1'">
          <cell title="已填性别" value="男"></cell>
        </template>
        <template v-else-if="userinfo.sex==='2'">
          <cell title="已填性别" value="女"></cell>
        </template> -->
        <!-- <cell title="性别" :value=userinfo.sex></cell> -->
        <selector v-model="userinfo.sex" title="性别" :options="sexoption"></selector>
        <cell title="邮箱" :value=userinfo.user_information_email>
          <x-input v-model="userinfo.user_information_email"></x-input>
        </cell>
        <cell title="手机号" :value=userinfo.user_information_cellphone>
          <x-input v-model="userinfo.user_information_cellphone"></x-input>
        </cell>
        <!-- <cell title="是否志愿者" :value="volornot">
        </cell> -->
      </group>
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" @click.native.prevent="handleCommituserinfomodify">提交</x-button>
      </group>
    </div>
</template>

<script>
import { Group, Cell, Blur, XButton, XInput, Selector } from 'vux'
import { commituserinfomodifyform, getDetailinfo } from '@/api/login'
export default {
  name: 'userInfomodify',
  components: { Group, Cell, Blur, XButton, XInput, Selector },
  data() {
    return {
      // userinfo: {
      //   url: 'https://o3e85j0cv.qnssl.com/tulips-1083572__340.jpg',
      //   name: this.content.user_information_name,
      //   sex: '',
      //   email: '',
      //   cellphone: '',
      //   volornot: ''
      // }
      // content: this.content,
      userinfo: this.userinfo,
      sexoption: [{
        key: '1',
        value: '男'
      }, {
        key: '2',
        value: '女'
      }]
      // user_name: this.userinfo.user_information_name,
      // url: 'https://o3e85j0cv.qnssl.com/tulips-1083572__340.jpg'
    }
  },
  created() {
    this.fetchData()
  // this.fetchImagelist()
  },
  methods: {
    fetchData() {
      getDetailinfo(window.localStorage.getItem('username')).then(response => {
        this.userinfo = response[0]
        // window.localStorage.setItem('campaignlists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
      console.log(this.userinfo.sex)
    },
    handleCommituserinfomodify() {
      const user_info_id = window.localStorage.getItem('user_info_id')
      const user_information_user_id = window.localStorage.getItem('user_id')
      const user_information_name = this.userinfo.user_information_name
      const user_information_sex = this.userinfo.user_information_sex
      const user_information_cellphone = this.userinfo.user_information_cellphone
      const user_information_email = this.userinfo.user_information_email
      const user_information_volunteer = false
      commituserinfomodifyform(
        user_info_id,
        user_information_user_id,
        user_information_name,
        user_information_sex,
        user_information_cellphone,
        user_information_email,
        user_information_volunteer
      ).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
        this.$router.push({ path: '/personal/userInfo' })
      }).catch(error => {
        console.log(error)
        // reject(error)
      })
    },
    onChange(val) {
      // console.log(val)
      console.log(this.userinfo.sex)
    }
  }
}
</script>

<style>
  #UserInfo .center {
    text-align: center;
    padding-top: 20px;
    color: #fff;
    font-size: 18px;
  }
  #UserInfo .center img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 4px solid #ececec;
  }
</style>

<!-- 个人基本信息包括修改,包括志愿者登记等
政策咨询->政策咨询列表
专业咨询->专业咨询列表
公益活动->已报名的公益活动
志愿服务->已报名的志愿服务
