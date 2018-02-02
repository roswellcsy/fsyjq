<!--用于填写登记志愿者信息 -->
<template>
  <div id ='VolunteerRegister'>
    <group>
        <cell title="姓名" value="value"></cell>
        <cell title="社区" value="value"></cell>
        <cell title="服务时间" value="value"></cell>
        .<br>
        .<br>
        .<br>
        .<br>
        <cell title="等等" value="value"></cell>
      </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'volunteerRegister',
  components: { Group, Cell }
}
</script>

<style>

</style>