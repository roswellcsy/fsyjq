<template>
    <div id="UserInfo">
      <blur :blur-amount=40 :url="url">
        <p class="center"><img :src="url"></p>
      </blur>
      <group title="个人信息">
        <cell title="用户名" is-link>{{ username }}</cell>
        <cell title="邮箱" value="value" is-link>{{ email }}</cell>
        <cell title="手机号" value="value" is-link>{{ cellphone }}</cell>
      <!-- <x-button type="primary" action-type="button" link="">登出</x-button> -->
      </group>
      <group title="服务信息">
        <cell title="我的专业咨询" link="/proAdv/index"></cell>
        <cell title="我的公益活动" link="/campaign/list"></cell>
        <cell title="我的志愿服务" link="/volServ/index"></cell>
      </group>
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" @click.native.prevent="handleFedLogOut">登出</x-button>
      </group>
    </div>
</template>

<script>
  import { Group, Cell, Blur, XButton } from 'vux'
  export default {
    name: 'userInfo',
    components: { Group, Cell, Blur, XButton },
    data() {
      return {
        url: 'https://o3e85j0cv.qnssl.com/tulips-1083572__340.jpg',
        username: this.$store.getters.username,
        email: this.$store.getters.email,
        cellphone: this.$store.getters.cellphone
      }
    },
    methods: {
      handleFedLogOut() { // 登出
        this.$store.dispatch('FedLogOut').then(() => {
          // this.loading = false
          this.$router.push({ path: '/login' })
        }).catch(() => {
          // this.loading = false
          console.log('something wrong')
        })
      }
    },
    created() {
      const vue = this
      vue.updateTitle('userInfo')
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
