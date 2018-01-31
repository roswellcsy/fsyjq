<template>
  <div id="login">
    <div class="vux-demo">
      <img class="logo" src="../../assets/vux_logo.png">
      <h1>登录</h1>
    </div>

    <group>
      <x-input title="账号" v-model="loginForm.username" placeholder="账号"></x-input>
      <x-input title="密码" @keyup.enter.native="handleLogin" v-model="loginForm.password" placeholder="密码"></x-input>
    </group>

    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleLogin">登录</x-button>
    </group>
    <div class="tips">
        <span style="margin-right:20px;">username: admin</span>
        <span> password: admin</span>
    </div>
  </div>
</template>

<script>
import { Group, Cell, XInput, XButton } from 'vux'

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
        this.$router.push({ path: '/' })
      }).catch(() => {
        // this.loading = false
        console.log('something wrong')
      })
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
