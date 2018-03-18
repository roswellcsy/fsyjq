/*
专业咨询api,提交专业咨询及查看自己已提交的专业咨询
*/

import request from '@/utils/request'

export function commitProadvform(
    proadv_user,
    proadv_question_title,
    proadv_question_type,
    proadv_question_content,
    proadv_full_name,
    proadv_sex,
    proadv_age,
    proadv_house_hold,
    proadv_id_num,
    proadv_ethnic,
    proadv_political_status,
    proadv_religion,
    proadv_occupation,
    proadv_studying_grade,
    proadv_degree_of_education,
    proadv_community,
    proadv_contact,
    proadv_live_address,
    proadv_marriage
) { // 提交政策咨询表单
  return request({
    // url: '/user/login', // 根据实际修改
    url: '/professonaladvice/',
    method: 'post',
    data: {
      // username,
      proadv_user,
      proadv_question_title,
      proadv_question_type,
      proadv_question_content,
      proadv_full_name,
      proadv_sex,
      proadv_age,
      proadv_house_hold,
      proadv_id_num,
      proadv_ethnic,
      proadv_political_status,
      proadv_religion,
      proadv_occupation,
      proadv_studying_grade,
      proadv_degree_of_education,
      proadv_community,
      proadv_contact,
      proadv_live_address,
      proadv_marriage
    }
  })
}

export function getMyProAdvlist(username) { // 拉取用户信息
  return request({
    url: '/professonaladvice/', // 获取admin信息，带用户名参数
    method: 'get',
    params: {
      username
    }
  })
}

export function getMyProAdv(proadv_question_title) { // 拉取用户信息
  return request({
    url: '/professonaladvice/', // 获取admin信息，带用户名参数
    method: 'get',
    params: {
      proadv_question_title
    }
  })
}
