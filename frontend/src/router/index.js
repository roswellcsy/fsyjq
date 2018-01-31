// import Vue from 'vue'
// import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

// Vue.use(Router)

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//   ]
// })
/* 根据vueAdmin-template修改! */

import Vue from 'vue'
import Router from 'vue-router'
const _import = require('./_import_' + process.env.NODE_ENV)
// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading
/**
 *  加载模块
 */
Vue.use(Router)

/* Layout */
// import INIT from '../views/layout/init'
/**
 *  路由配置
 */
export const constantRouterMap = [
  { path: '/login', component: _import('login/index') },
  { path: '/404', component: _import('404'), hidden: true },
  {
    path: '/',
    component: _import('layout/init'),
    // redirect: '/init',
    name: 'init',
    hidden: true,
    children: [
      {
        path: 'personal/userInfo',
        name: 'userInfo',
        component: _import('personal/userInfo'),
        meta: { title: '主页' }
      },
      {
        path: 'home',
        name: 'home',
        component: _import('home'),
        meta: { title: '主页' }
      }
    ]
  }
  // { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})
// const router = new VueRouter({
//   base: __dirname,
//   likActiveClass: 'link-active',
//   routes: [
//     {
//       path: '/init',
//       name: 'init',
//       component: resolve => require(['../components/init.vue'], resolve),
//       children: [
//         {
//           path: 'personal/userInfo',
//           name: 'userInfo',
//           component: resolve => require(['../components/personal/userInfo.vue'], resolve),
//           meta: { title: '主页' }
//         },
//         {
//           path: 'home',
//           name: 'home',
//           component: resolve => require(['../components/home.vue'], resolve),
//           meta: { title: '主页' }
//         }
//       ]
//     },
//     {
//       path: '/login',
//       name: 'login',
//       component: resolve => require(['../components/login.vue'], resolve),
//       meta: { title: '登录' }
//     }
//   ]
// })
/**
 *  路由出口
 */
// export default router
