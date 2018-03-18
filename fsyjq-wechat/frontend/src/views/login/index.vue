<template>
  <div id="login">
    <div class="vux-demo">
      <img class="logo" src="../../assets/profile.png">
      <h1>登录</h1>
    </div>

    <group>
      <x-input title="账号" v-model="loginForm.username" placeholder="必填"></x-input>
      <x-input title="密码" type="password" @keyup.enter.native="handleLogin" v-model="loginForm.password" placeholder="必填"></x-input>
    </group>
    <!-- <div class="tips">
        <span style="margin-left:40%;">请先登录</span>
    </div> -->
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleLogin">登录</x-button>
    </group>
    <!-- <div class="tips">
        <span style="margin-left:40%;">或注册</span>
    </div> -->
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" link="/register">注册</x-button>
    </group>
  </div>
</template>

<script>
import { Group, Cell, XInput, XButton } from 'vux'
// import { volinfoinit } from '@/api/login'

export default {
  name: 'login',
  components: {
    Group,
    Cell,
    XInput,
    XButton
  },
  data() {
    return {
      loginForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    // login() {
    //   let vue = this;
    //   vue.$router.push({ name: "userInfo", params: {} });
    // }
    handleLogin() {
    //   this.loginForm.validate(valid => {
    //     if (valid) {
    //       // this.loading = true
    //       this.$store.dispatch('Login', this.loginForm).then(() => {
    //         // this.loading = false
    //         this.$router.push({ path: '/' })
    //       }).catch(() => {
    //         // this.loading = false
    //       })
    //     } else {
    //       console.log('error submit!!')
    //       return false
    //     }
    //   // })
    // }
      this.$store.dispatch('Login', this.loginForm).then(() => {
        // this.loading = false
        this.$router.push({ path: '/personal/userInfo' })
      }).catch(() => {
        // this.loading = false
        console.log('something wrong')
      })
      // userinfoinit(username).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
      //   // this.$router.push({ path: '/login' })
      // }).catch(error => {
      //   console.log(error)
      //   // reject(error)
      // })
      // volinfoinit(this.loginForm.username, this.loginForm.password).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
      //   // this.$router.push({ path: '/login' })
      // }).catch(error => {
      //   console.log(error)
      //   // reject(error)
      // })
    }
  }
}
</script>

<style>
.vux-demo {
  text-align: center;
}
.logo {
  width: 100px;
  height: 100px;
}
</style>
