<!--用于展示专业咨询、公益活动、志愿服务一级目录 -->
<template>
  <div id ='CharityCampaign'>
    <group>
        <cell title="专业咨询" link="/proAdv/index"></cell>
        <cell title="公益活动" link="/campaign/list"></cell>
        <cell title="志愿者服务" link="/volServ/index"></cell>
    </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'charityCampaign',
  components: { Group, Cell }
}
</script>

<style>

</style>