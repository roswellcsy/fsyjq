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
    url: '/participate/campaign/',
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

export function campaignSignup(campaign_id, user_id) {
  return request({
    url: '/campaign/signup/' + campaign_id + '/',
    method: 'put',
    data: {
      'campaign_members_ids': [user_id]
    }
  })
}
