import request from '@/utils/request'

export function login(username, password) {
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

export function getInfo(token) {
  return request({
    url: '/user/3', // 获取admin信息，后期需要改
    method: 'get',
    params: { token }
  })
}

export function logout() { // 后端方法需要改！
  return request({
    url: '/user/logout',
    method: 'post'
  })
}
