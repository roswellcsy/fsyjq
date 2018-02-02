<!--用于展示户籍相关政策清单 
后续改为模板形式
-->
<template>
  <div id ='huji'>
    <group>
      <!-- <cell title="政策信息" link="/policy/policyList"></cell> -->
      <cell title="引进人才入户须知" link="http://119.145.135.223/Mobile/Article/ArticleDetail.aspx?ID=26&UserID=3"></cell>
      <cell title="在我市常住的非本市户籍人员入户须知" link="http://119.145.135.223/Mobile/Article/ArticleDetail.aspx?ID=28&UserID=3"></cell>
      <cell title="佛山市异地务工人员积分入户指标及分值表" link="http://119.145.135.223/Mobile/Article/ArticleDetail.aspx?ID=25&UserID=3"></cell>
      <cell title="佛山市新市民积分制服务管理暂行办法" link="http://119.145.135.223/Mobile/Article/ArticleDetail.aspx?ID=57&UserID=3"></cell>
    </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'huji',
  components: { Group, Cell }
}
</script>

<style>

</style>