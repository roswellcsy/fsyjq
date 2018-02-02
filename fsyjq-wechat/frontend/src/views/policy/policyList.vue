<!--用于展示政策清单 
后续改为模板形式
-->
<template>
  <div id ='PolicyList'>
    <group>
      <!-- <cell title="政策信息" link="/policy/policyList"></cell> -->
      <cell title="居住证及相关" link="/policy/juzhuzheng"></cell>
      <cell title="户籍及相关" link="/policy/huji"></cell>
      <cell title="计生及相关" link="/policy/jisheng"></cell>
      <cell title="住房及相关" link="/policy/zhufang"></cell>
      <cell title="子女教育及相关" link="/policy/zinvjiaoyu"></cell>
    </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'policyList',
  components: { Group, Cell }
}
</script>

<style>

</style>