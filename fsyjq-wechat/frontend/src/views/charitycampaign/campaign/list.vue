<!--用于展示公益活动清单 -->
<template>
  <div id ='CampaignList'>
    <group>
        <cell title="活动一" link="/campaign/detail"></cell>
        <cell title="活动二" link="/campaign/detail"></cell>
        <cell title="活动三" link="/campaign/detail"></cell>
    </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'campaignList',
  components: { Group, Cell }
}
</script>

<style>

</style>