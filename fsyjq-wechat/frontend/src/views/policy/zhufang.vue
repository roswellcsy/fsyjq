<!--用于展示住房相关政策清单 
后续改为模板形式
-->
<template>
  <div id ='zhufang'>
    <group>
      <!-- <cell title="政策信息" link="/policy/policyList"></cell> -->
      <cell title="佛山市人民政府关于印发佛山市保障性住房管理办法的通知" link="http://119.145.135.223/Mobile/Article/ArticleDetail.aspx?ID=14&UserID=3"></cell>
      <cell title="异地务工人员住房保障服务" link="http://119.145.135.223/Mobile/Article/ArticleDetail.aspx?ID=13&UserID=3"></cell>
      <cell title="佛山市保障性住房管理办法" link="http://119.145.135.223/Mobile/Article/ArticleDetail.aspx?ID=12&UserID=3"></cell>
      <cell title="佛山市居住房屋出租管理暂行办法" link="http://119.145.135.223/Mobile/Article/ArticleDetail.aspx?ID=56&UserID=3"></cell>
    </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'zhufang',
  components: { Group, Cell }
}
</script>

<style>

</style>