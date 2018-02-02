<!--用于展示政策和政策咨询一级目录 -->

<template>
  <div id ='Policy'>
    <group>
      <!-- <cell title="政策信息" link="/policy/policyList"></cell> -->
      <cell title="服务政策" link="/policy/policyList"></cell>
      <cell title="禅城区积分制政策" link="http://119.145.135.223/Mobile/Article/ArticleList.aspx?UserID=3&OpenID=oWmDUs1HRVsFKRA1XAprP7PNV7WE&KeyWord=%E7%A6%85%E5%9F%8E%E5%8C%BA"></cell>
      <cell title="南海区积分制政策" link="http://119.145.135.223/Mobile/Article/ArticleList.aspx?UserID=3&OpenID=oWmDUs1HRVsFKRA1XAprP7PNV7WE&KeyWord=%E5%8D%97%E6%B5%B7%E5%8C%BA"></cell>
      <cell title="顺德区积分制政策" link="http://119.145.135.223/Mobile/Article/ArticleList.aspx?UserID=3&OpenID=oWmDUs1HRVsFKRA1XAprP7PNV7WE&KeyWord=%E9%A1%BA%E5%BE%B7%E5%8C%BA"></cell>
      <cell title="高明区积分制政策" link="http://119.145.135.223/Mobile/Article/ArticleList.aspx?UserID=3&OpenID=oWmDUs1HRVsFKRA1XAprP7PNV7WE&KeyWord=%E9%AB%98%E6%98%8E%E5%8C%BA"></cell>
      <cell title="三水区积分制政策" link="http://119.145.135.223/Mobile/Article/ArticleList.aspx?UserID=3&OpenID=oWmDUs1HRVsFKRA1XAprP7PNV7WE&KeyWord=%E4%B8%89%E6%B0%B4%E5%8C%BA"></cell>
      <cell title="自助申报" link="http://zjsb.fslgb.gov.cn/wx/main"></cell>
      <cell title="政策咨询" link="/policy/policyQa"></cell>
    </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'policy',
  components: { Group, Cell }
}
</script>

<style>

</style>