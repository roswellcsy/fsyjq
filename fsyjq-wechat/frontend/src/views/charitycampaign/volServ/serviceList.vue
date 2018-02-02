<!--用于展示志愿服务清单 -->
<template>
  <div id ='ServiceList'>
    <group>
        <cell title="服务一" value="value" link=""></cell>
        <cell title="服务二" value="value" link=""></cell>
        <cell title="服务三" value="value" link=""></cell>
        .<br>
        .<br>
        .<br>
        .<br>
        <cell title="等等" value="value" link=""></cell>
      </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'serviceList',
  components: { Group, Cell }
}
</script>

<style>

</style>