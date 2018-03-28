<!--用于展示志愿者登记、能力培训、志愿服务二级目录 -->
<template>
  <div id ='VolServ'>
    <template v-if="vol_info_id !== null">
      <group>
        <!-- <cell title="志愿者登记" link="/volServ/register"></cell> -->
        <cell title="能力培训" link="/volServ/traningList"></cell>
        <cell title="志愿服务" link="/volServ/serviceList"></cell>
      </group>
    </template>
    <template v-else-if="vol_info_id === null">
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" link="/volServ/register">请先登记成为志愿者</x-button>
      </group>
    </template>
  </div>
</template>

<script>
import { Group, Cell, XButton } from 'vux'
export default {
  name: 'volServ',
  components: { Group, Cell, XButton },
  data() {
    return {
      vol_info_id: window.localStorage.getItem('vol_info_id')
    }
  }
}
</script>

<style>

</style>