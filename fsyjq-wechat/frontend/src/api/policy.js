/*
政策相关api,获取政策文章列表及详细列表,政策咨询提交及查看自己的
*/

import request from '@/utils/request'

export function commitPolicyqaform(
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
    url: '/policyqa/',
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

export function getMyPolicyQAlist(username) { // 拉取用户信息
  return request({
    url: '/policyqa/', // 获取admin信息，带用户名参数
    method: 'get',
    params: {
      username
    }
  })
}

export function getMyPolicyQA(qa_title) { // 拉取用户信息
  return request({
    url: '/policyqa/', // 获取admin信息，带用户名参数
    method: 'get',
    params: {
      qa_title
    }
  })
}
