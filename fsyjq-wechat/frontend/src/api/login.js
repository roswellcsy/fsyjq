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

export function getInfo(username) { // 拉取用户信息
  return request({
    url: '/user/', // 获取admin信息，带用户名参数
    method: 'get',
    params: {
      username
    }
  })
}

export function getDetailinfo(username) { // 拉取用户信息
  return request({
    url: '/userinformation/', // 获取admin信息，带用户名参数
    method: 'get',
    params: {
      username
    }
  })
}

export function commituserinfocreateform(
  user_information_user_id,
  user_information_name,
  user_information_sex,
  user_information_cellphone,
  user_information_email,
  user_information_volunteer
) { // 拉取用户信息
  return request({
    url: '/userinformation/',
    method: 'post',
    data: {
      user_information_user_id,
      user_information_name,
      user_information_sex,
      user_information_cellphone,
      user_information_email,
      user_information_volunteer
    }
  })
}

export function commituserinfomodifyform(
  user_info_id,
  user_information_user_id,
  user_information_name,
  user_information_sex,
  user_information_cellphone,
  user_information_email,
  user_information_volunteer
) { // 拉取用户信息
  return request({
    url: '/userinformation/' + user_info_id + '/',
    method: 'put',
    data: {
      user_information_user_id,
      user_information_name,
      user_information_sex,
      user_information_cellphone,
      user_information_email,
      user_information_volunteer
    }
  })
}

export function register(username, password) { // 注册
  return request({
    // url: '/user/login', // 根据实际修改
    url: '/api-register/',
    method: 'post',
    data: {
      username,
      password
    }
  })
}

// export function userinfoinit(username) { // 注册
//   return request({
//     // url: '/user/login', // 根据实际修改
//     url: '/api-register/',
//     method: 'post',
//     data: {
//       // username,
//       username
//     }
//   })
// }

// export function volinfoinit(
//   username,
//   password
// ) { // 注册
//   return request({
//     // url: '/user/login', // 根据实际修改
//     url: '/volunteerinformation/',
//     method: 'post',
//     data: {
//       volinfo_marriage: '1',
//       volinfo_idcard_type: '1',
//       volinfo_service_date: '1',
//       volinfo_service_time: 0,
//       volinfo_user: {
//         username,
//         password
//       }
//     }
//   })
// }

// export function logout() { // 后端方法需要改！目前没有这个方法
//   return request({
//     url: '/user/logout',
//     method: 'post'
//   })
// }
