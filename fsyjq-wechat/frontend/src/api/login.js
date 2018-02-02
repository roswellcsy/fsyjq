/*
登录注册api
*/

import request from '@/utils/request'

export function login(username, password) { // 登录
  return request({
    // url: '/user/login', // 根据实际修改
    url: '/token-api-auth/login/',
    method: 'post',
    data: {
      // username,
      username,
      password
    }
  })
}

export function getInfo(username, token) { // 拉取用户信息
  return request({
    url: '/user/', // 获取admin信息，后期需要改成带用户名参数
    method: 'get',
    params: {
      username,
      token
    }
  })
}

export function register(username, password, cellphone, email) { // 注册
  return request({
    // url: '/user/login', // 根据实际修改
    url: '/api-register/',
    method: 'post',
    data: {
      // username,
      username,
      password,
      cellphone,
      email
    }
  })
}

// export function logout() { // 后端方法需要改！目前没有这个方法
//   return request({
//     url: '/user/logout',
//     method: 'post'
//   })
// }
