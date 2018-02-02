<!--用于展示政策和政策咨询一级目录 -->

<template>
  <div id ='Policy'>
    <group>
        <cell title="政策信息" link="/policy/policyList"></cell>
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