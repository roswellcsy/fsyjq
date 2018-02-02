<!--用于展示志愿者登记、能力培训、志愿服务二级目录 -->
<template>
  <div id ='VolServ'>
    <group>
        <cell title="志愿者登记" link="/volServ/register"></cell>
        <cell title="能力培训" link="/volServ/traningList"></cell>
        <cell title="志愿服务" link="/volServ/serviceList"></cell>
    </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'volServ',
  components: { Group, Cell }
}
</script>

<style>

</style>