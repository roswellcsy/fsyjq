<template>
    <div id="UserInfo">
      <blur :blur-amount=40 :url="url">
        <p class="center"><img :src="url"></p>
      </blur>
      <template v-if="content !== null">
        <group title="个人信息">
          <cell title="账号" :value=username></cell>
          <template v-if="content.user_information_name === null">
            <cell title="姓名" value=""></cell>
          </template>
          <template v-else-if="content.user_information_name !== null">
            <cell title="姓名" :value=content.user_information_name></cell>
          </template>
          <template v-if="content.user_information_sex === '1'">
            <cell title="性别" value="男"></cell>
          </template>
          <template v-if="content.user_information_sex === '2'">
            <cell title="性别" value="女"></cell>
          </template>
          <template v-if="content.user_information_email === null">
            <cell title="邮箱" value="无"></cell>
          </template>
          <template v-if="content.user_information_email !== null">
            <cell title="邮箱" :value=content.user_information_email></cell>
          </template>
          <cell title="手机号" :value=content.user_information_cellphone></cell>
          <template v-if="volinfo === null">
            <cell title="是否志愿者" value="否"></cell>
            <cell title="志愿服务时数" value="无"></cell>
          </template>
          <template v-else-if="volinfo !== null">
            <cell title="是否志愿者" value="是"></cell>
            <cell title="志愿服务时数" :value=volinfo.volinfo_service_time></cell>
          </template>
        </group>
      </template>
      <template v-else-if="content === null">
        <group title="个人信息">
          <cell title="账号" :value=username></cell>
          <cell title="姓名" value="">请添加个人信息</cell>
          <cell title="性别" value="">请添加个人信息</cell>
          <cell title="邮箱" value="">请添加个人信息</cell>
          <cell title="手机号" value="">请添加个人信息</cell>
          <template v-if="volinfo === null">
            <cell title="是否志愿者" value="">否</cell>
            <cell title="志愿服务时数" value="">无</cell>
          </template>
          <template v-else-if="volinfo !== null">
            <cell title="是否志愿者" value="">是</cell>
            <cell title="志愿服务时数" :value=volinfo.volinfo_service_time></cell>
          </template>
        </group>
      </template>
      <template v-if="content === null">
        <group style="padding:5px 20px;">
          <x-button type="primary" action-type="button" link="/personal/userInfocreate">添加个人信息</x-button>
        </group>
      </template>
      <template v-else-if="content !== null">
        <group style="padding:5px 20px;">
          <x-button type="primary" action-type="button" link="/personal/userInfomodify">修改个人信息</x-button>
        </group>
      </template>
      <template v-if="volinfo === null">
        <group style="padding:5px 20px;">
          <x-button type="primary" action-type="button" link="/volServ/register">志愿者登记</x-button>
        </group>
      </template>
      <template v-else-if="volinfo !== null">
        <group style="padding:5px 20px;">
          <x-button type="primary" action-type="button" link="/volServ/modify">修改志愿者信息</x-button>
        </group>
      </template>
      <group title="服务信息">
        <cell title="我的政策咨询" link="/personal/userPolicyQAlist"></cell>
        <cell title="我的专业咨询" link="/personal/userProAdvlist"></cell>
        <cell title="我的公益活动" link="/personal/userCampaignlist"></cell>
        <cell title="我的志愿服务" link="/personal/userVolServlist"></cell>
        <cell title="我的能力培训" link="/personal/userTraininglist"></cell>
      </group>
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" @click.native.prevent="handleFedLogOut">登出</x-button>
      </group>
      <!-- <template v-if="volid === null">
        <h1>不是志愿者</h1>
      </template>
      <template v-else-if="volid !== null">
        <h1>是志愿者</h1>
      </template> -->
    </div>
</template>

<script>
import { Group, Cell, Blur, XButton } from 'vux'
import { getDetailinfo } from '@/api/login'
import { getVolinfo } from '@/api/volunteer'
export default {
  name: 'userInfo',
  components: { Group, Cell, Blur, XButton },
  data() {
    return {
      url: 'https://o3e85j0cv.qnssl.com/tulips-1083572__340.jpg',
      // username: window.localStorage.username,
      // sex: this.sex,
      // email: window.localStorage.email,
      // cellphone: window.localStorage.cellphone,
      // volornot: this.volornot,
      username: window.localStorage.getItem('username'),
      // volid: window.localStorage.getItem('vol_info_id'),
      // userinfoid: window.localStorage.getItem('user_info_id'),
      content: this.content,
      volinfo: this.volinfo
    }
  },
  methods: {
    // detail2string() {
    //   if (this.content.user_information_sex === '1') {
    //     this.sex = '男'
    //   } else {
    //     this.sex = '女'
    //   }
    //   if (window.localStorage.volornot === true) {
    //     this.volornot = '是'
    //   } else {
    //     this.volornot = '否'
    //   }
    // },
    fetchData() {
      getDetailinfo(window.localStorage.getItem('username')).then(response => {
        if (response.length === 0) {
          this.content = null
        } else {
          this.content = response[0]
        }
        // window.localStorage.setItem('campaignlists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
      getVolinfo(window.localStorage.getItem('username')).then(response => {
        if (response.length === 0) {
          this.volinfo = null
        } else {
          this.volinfo = response[0]
        }
        // window.localStorage.setItem('campaignlists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
    },
    handleFedLogOut() { // 登出
      this.$store.dispatch('FedLogOut').then(() => {
        // this.loading = false
        window.localStorage.clear()
        this.$router.push({ path: '/login' })
      }).catch(() => {
        // this.loading = false
        console.log('something wrong')
      })
    }
  },
  created() {
    this.fetchData()
    // this.detail2string()
  //   const vue = this
  //   vue.updateTitle('userInfo')
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
