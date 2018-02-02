<!--用于展示志愿服务详情及报名 -->
<template>
  <div id ='ServiceDetail'>
    <group>
        <cell title="主讲人" value="value"></cell>
        <cell title="地址" value="value"></cell>
        <cell title="举办时间" value="value"></cell>
        .<br>
        .<br>
        .<br>
        .<br>
        <cell title="截止时间" value="value"></cell>
      </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'serviceDetail',
  components: { Group, Cell }
}
</script>

<style>

</style>