/*
专业咨询api,提交专业咨询及查看自己已提交的专业咨询
*/

import request from '@/utils/request'

export function commitProadvform(
    qa_user,
    qa_fullname,
    qa_sex,
    qa_age,
    qa_live_area,
    qa_cellphone,
    qa_occupation,
    qa_marriage,
    qa_title,
    qa_type,
    qa_content,
    qa_o2o
) { // 提交政策咨询表单
  return request({
    // url: '/user/login', // 根据实际修改
    url: '/proadv/',
    method: 'post',
    data: {
      // username,
      qa_user,
      qa_fullname,
      qa_sex,
      qa_age,
      qa_live_area,
      qa_cellphone,
      qa_occupation,
      qa_marriage,
      qa_title,
      qa_type,
      qa_content,
      qa_o2o
    }
  })
}

export function getMyProAdv(username, token) { // 拉取用户信息
  return request({
    url: '/proadv/', // 获取admin信息，带用户名参数
    method: 'get',
    params: {
      username,
      token
    }
  })
}
