// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import FastClick from 'fastclick'
// import zh_CN from 'vee-validate/dist/locale/zh_CN'
import VeeValidate from 'vee-validate'

// import VueRouter from 'vue-router'
import App from './App'
// import Home from './components/HelloFromVux'
// Validator.addLocale(zh_CN)
import {
  WechatPlugin,
  AjaxPlugin,
  LoadingPlugin,
  ToastPlugin,
  AlertPlugin
} from 'vux'
import router from './router'
import Vuex from 'vuex'
// 新增
import store from './store'
import '@/permission' // permission control

// Vue.use(VueRouter)
/**
 * 加载插件
 */
Vue.use(
  VeeValidate
)
Vue.use(Vuex)
Vue.use(WechatPlugin)
Vue.use(AjaxPlugin)
Vue.use(LoadingPlugin)
Vue.use(ToastPlugin)
Vue.use(AlertPlugin)
/**
 * 设置vuex
 */
// const store = new Vuex.Store({})
// store.registerModule('vux', {
//   state: {
//     loading: false,
//     showBack: true,
//     title: '',
//     number: ''
//   },
//   mutations: {
//     updateLoading(state, loading) {
//       state.loading = loading
//     },
//     updateShowBack(state, showBack) {
//       state.showBack = showBack
//     },
//     updateTitle(state, title) {
//       state.title = title
//     },
//     updateNumber(state, number) {
//       let num = ''
//       if (number <= 0) {
//         state.number = num
//       } else {
//         num = number.toString()
//         state.number = num
//       }
//     }
//   }
// })
/**
 * 公用组件
 */
// Vue.prototype.updateTitle = function(value) {
//   this.$store.commit('updateTitle', value)
// }
/**
 *  日志输出开关
 */
Vue.config.productionTip = true
/**
 *  点击延迟
 */
FastClick.attach(document.body)

// const routes = [{
//   path: '/',
//   component: Home
// }]

// const router = new VueRouter({
//   routes
// })

// FastClick.attach(document.body)

// Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
//   store,
//   router,
//   render: h => h(App)
// }).$mount('#app-box')
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
