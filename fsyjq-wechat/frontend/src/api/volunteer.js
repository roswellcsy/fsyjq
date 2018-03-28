/*
志愿者相关api,提交志愿者登记信息,获取志愿者服务列表(已发布的,已报名的)、获取能力培训列表(已发布的，已报名的)，报名志愿者服务，报名能力培训
*/

import request from '@/utils/request'

export function fetchPublishedlist() {
  return request({
    url: '/campaign/published/',
    method: 'get'
  //   params: query
  })
}

export function fetchMylist(username) {
  return request({
    url: '/participate/volunteerservice/',
    method: 'get',
    params: {
      username
    }
  })
}

export function fetchCurrentvolservice(campaign_name) {
  return request({
    url: '/campaign/published/',
    method: 'get',
    params: {
      campaign_name
    }
  })
}

export function volserviceSignup(campaign_id, user_id) {
  return request({
    url: '/volserivce/signup/' + campaign_id + '/',
    method: 'put',
    data: {
      'campaign_volunteers_ids': [user_id]
    }
  })
}

export function fetchTraininglist() {
  return request({
    url: '/training/published/',
    method: 'get'
    // params: {
    //   username
    // }
  })
}

export function fetchMyTraininglist(username) {
  return request({
    url: '/training/published/',
    method: 'get',
    params: {
      username
    }
  })
}

export function fetchCurrentTraining(at_theme) {
  return request({
    url: '/training/published/',
    method: 'get',
    params: {
      at_theme
    }
  })
}

export function TrainingSignup(at_id, user_id) {
  return request({
    url: '/training/published/' + at_id + '/',
    method: 'put',
    data: {
      'volunteers_ids': [user_id]
    }
  })
}

export function commitvolregisterform(
  volinfo_user_id,
  volinfo_jiguan,
  volinfo_live_address,
  volinfo_marriage,
  volinfo_idcard_type,
  volinfo_id_num,
  volinfo_birthday,
  volinfo_graduate_school,
  volinfo_graduate_date,
  volinfo_education,
  volinfo_profession,
  volinfo_employer,
  volinfo_position,
  volinfo_mail_address,
  volinfo_zipcode,
  volinfo_contact_number,
  volinfo_service_area,
  volinfo_service_date,
  volinfo_skills
) { // 提交政策咨询表单
  return request({
    // url: '/user/login', // 根据实际修改
    url: '/volunteerinformation/',
    method: 'post',
    data: {
      // username,
      volinfo_user_id,
      volinfo_jiguan,
      volinfo_live_address,
      volinfo_marriage,
      volinfo_idcard_type,
      volinfo_id_num,
      volinfo_birthday,
      volinfo_graduate_school,
      volinfo_graduate_date,
      volinfo_education,
      volinfo_profession,
      volinfo_employer,
      volinfo_position,
      volinfo_mail_address,
      volinfo_zipcode,
      volinfo_contact_number,
      volinfo_service_area,
      volinfo_service_date,
      volinfo_skills,
      volinfo_service_time: 0
    }
  })
}

export function commitvolmodifyform(
  vol_info_id,
  volinfo_user_id,
  volinfo_jiguan,
  volinfo_live_address,
  volinfo_marriage,
  volinfo_idcard_type,
  volinfo_id_num,
  volinfo_birthday,
  volinfo_graduate_school,
  volinfo_graduate_date,
  volinfo_education,
  volinfo_profession,
  volinfo_employer,
  volinfo_position,
  volinfo_mail_address,
  volinfo_zipcode,
  volinfo_contact_number,
  volinfo_service_area,
  volinfo_service_date,
  volinfo_skills
) { // 提交志愿者信息修改表单
  return request({
    // url: '/user/login', // 根据实际修改
    url: '/volunteerinformation/' + vol_info_id + '/',
    method: 'put',
    data: {
      // username,
      volinfo_user_id,
      volinfo_jiguan,
      volinfo_live_address,
      volinfo_marriage,
      volinfo_idcard_type,
      volinfo_id_num,
      volinfo_birthday,
      volinfo_graduate_school,
      volinfo_graduate_date,
      volinfo_education,
      volinfo_profession,
      volinfo_employer,
      volinfo_position,
      volinfo_mail_address,
      volinfo_zipcode,
      volinfo_contact_number,
      volinfo_service_area,
      volinfo_service_date,
      volinfo_skills
    }
  })
}

export function getVolinfo(username) { // 拉取用户信息
  return request({
    url: '/volunteerinformation/', // 获取admin信息，带用户名参数
    method: 'get',
    params: {
      username
    }
  })
}
