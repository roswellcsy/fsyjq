<template>
    <div id="UserInfoCreate">
      <!-- <blur :blur-amount=40 :url="url">
        <p class="center"><img :src="url"></p>
      </blur> -->
      <group title="个人信息">
        <cell title="姓名">
          <x-input v-model="userinfo.name"></x-input>
        </cell>
        <!-- <cell title="性别"> -->
          <!-- <x-input v-model="userinfo.sex"></x-input> -->
        <!-- <group title="性别"> -->
          <!-- <picker :data='sexoption' :columns=1 v-model="userinfo.sex" @on-change='change'></picker> -->
        <selector title="性别" v-model="userinfo.sex" :options="sexoption" @on-change="onChange"></selector>
        <!-- </group> -->
        <!-- </cell> -->
        <cell title="邮箱">
          <x-input v-model="userinfo.email"></x-input>
        </cell>
        <cell title="手机号">
          <x-input v-model="userinfo.cellphone"></x-input>
        </cell>
        <!-- <cell title="是否志愿者" value="value" is-link>
          <x-input v-model="volinfo.jiguan" :placeholder=content.volinfo_jiguan></x-input>
        </cell> -->
      </group>
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" @click.native.prevent="handleCommituserinfocreate">提交</x-button>
      </group>
    </div>
</template>

<script>
import { Group, Cell, Blur, XButton, XInput, Picker, Selector } from 'vux'
import { commituserinfocreateform } from '@/api/login'
export default {
  name: 'userInfomodify',
  components: { Group, Cell, Blur, XButton, XInput, Picker, Selector },
  data() {
    return {
      userinfo: {
        // url: 'https://o3e85j0cv.qnssl.com/tulips-1083572__340.jpg',
        name: '',
        sex: '',
        email: '',
        cellphone: '',
        volornot: ''
      },
      sexoption: [{
        value: '男',
        key: '1'
      }, {
        value: '女',
        key: '2'
      }]
      // test: [{ key: '1', value: '男' }, { key: '2', value: '女' }],
      // testvalue: []
      // content: this.content
    }
  },
  created() {
  // this.fetchData()
  // this.fetchImagelist()
  },
  methods: {
    // fetchData() {
    //   getDetailinfo(window.localStorage.getItem('username')).then(response => {
    //     this.content = response[0]
    //     // window.localStorage.setItem('campaignlists', this.lists)
    //   }).catch(err => {
    //     // this.fetchSuccess = false
    //     console.log(err)
    //   })
    // },
    handleCommituserinfocreate() {
      const user_information_user_id = window.localStorage.getItem('user_id')
      const user_information_name = this.userinfo.name
      const user_information_sex = this.userinfo.sex
      const user_information_cellphone = this.userinfo.cellphone
      const user_information_email = this.userinfo.email
      const user_information_volunteer = false
      commituserinfocreateform(
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
