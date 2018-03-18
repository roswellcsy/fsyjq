import router from './router'
import store from './store'
import NProgress from 'nprogress' // Progress 进度条
import 'nprogress/nprogress.css'// Progress 进度条样式
// import { Message } from 'element-ui'
import { getToken } from '@/utils/auth' // 验权

const whiteList = [
  // '/login',
  // '/register'
  '/login/index',
  '/register/index',
  '/policy',
  '/policy/index',
  '/policy/policyList',
  '/charitycampaign',
  '/charitycampaign/index',
  '/campaign/list',
  '/campaign/detail',
  '/volServ/index',
  '/volServ/traningList',
  '/volServ/trainingDetail',
  '/volServ/serviceList',
  '/volServ/serviceDetail',
  '/shareplatform',
  '/shareplatform/index',
  '/policy/juzhuzheng',
  '/policy/huji',
  '/policy/jisheng',
  '/policy/zhufang',
  '/policy/zinvjiaoyu',
  '/policy/policyJifen'
  // // 调试，生产需要注销
  // '/policy/policyQa',
  // '/proAdv/index',
  // '/volServ/register',
  // '/volServ/traningList',
  // '/personal/userPolicyQA',
  // '/personal/userProAdv',
  // '/personal/userCampaign',
  // '/personal/userVolServ'
] // 不重定向白名单
router.beforeEach((to, from, next) => {
  NProgress.start()
  if (getToken()) { // 判断是否有token
    if (to.path === '/login') { // 有token，判断是否前往登录界面
      next({ path: '/' }) // 因为有token，即认证过，前往登录界面则直接转至/dashboard
    } else {
      if (store.getters.user_id.length === 0) {
        // 只有在login阶段才会获取到username，
        // 然后才是根据getinfo拉到对应username的信息，
        // 否则重新登录，避免刷新丢失state的username
        store.dispatch('GetInfo').then(res => { // 拉取用户信息
          next()
        }).catch(() => {
          store.dispatch('FedLogOut').then(() => { // 失败，重新登录
            // Message.error('验证失败,请重新登录') /* 根据VUX的提示修改 */
            console.log('验证失败,请重新登录')
            next({ path: '/login' })
          })
        })
        store.dispatch('GetDetailInfo').then(res => { // 拉取用户信息
          next()
        })
        store.dispatch('GetVolInfo').then(res => { // 拉取用户信息
          next()
        })
      } else {
        next()
        // store.dispatch('FedLogOut').then(() => { // 失败，重新登录
        //   // Message.error('验证失败,请重新登录') /* 根据VUX的提示修改 */
        //   console.log('验证失败,请重新登录')
        //   next({ path: '/login' })
        // })
      }
    }
  } else {
    if (whiteList.indexOf(to.path) !== -1) { // 在免登录白名单，直接进入
      next()
    } else {
      next('/login') // 不在白名单，无论如何最终都是重定向到/login页面
      NProgress.done()
    }
  }
})

router.afterEach(() => {
  NProgress.done() // 结束Progress
})
