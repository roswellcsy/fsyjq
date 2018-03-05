/*
公益活动api,获取公益活动列表,报名公益活动
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
    url: '/campaign/published/',
    method: 'get',
    params: {
      username
    }
  })
}

export function fetchCurrentcampaign(campaign_name) {
  return request({
    url: '/campaign/published/',
    method: 'get',
    params: {
      campaign_name
    }
  })
}
