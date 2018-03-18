<template>
  <div id="register">
    <div class="vux-demo">
      <img class="logo" src="../../assets/profile.png">
      <h1>注册</h1>
    </div>

    <group>
      <x-input title="账号" v-model="RegisterForm.username" placeholder="必填（建议使用手机号）"></x-input>
      <x-input title="密码" type="password" v-model="RegisterForm.password" placeholder="请注意保管"></x-input>
    </group>

    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleRegister">注册</x-button>
    </group>
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" link="/login">返回登录</x-button>
    </group>
    <!-- <div class="tips">
        <span style="margin-left:40%;">请先注册</span>
        <span> password: admin</span>
    </div> -->
  </div>
</template>

<script>
import { Group, Cell, XInput, XButton } from 'vux'
import { register } from '@/api/login'

export default {
  name: 'register',
  components: {
    Group,
    Cell,
    XInput,
    XButton
  },
  data() {
    return {
      RegisterForm: {
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
    handleRegister() {
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
      const username = this.RegisterForm.username
      const password = this.RegisterForm.password
      register(username, password).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
        this.$router.push({ path: '/login' })
      }).catch(error => {
        console.log(error)
        // reject(error)
      })
      // userinfoinit(username).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
      //   // this.$router.push({ path: '/login' })
      // }).catch(error => {
      //   console.log(error)
      //   // reject(error)
      // })
      // volinfoinit(username, password).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
      //   // this.$router.push({ path: '/login' })
      // }).catch(error => {
      //   console.log(error)
      //   // reject(error)
      // })
      // this.$store.dispatch('Register', this.RegisterForm).then(() => {
      //   // this.loading = false
      //   this.$router.push({ path: '/login' })
      // }).catch(() => {
      //   // this.loading = false
      //   console.log('something wrong while registering')
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
