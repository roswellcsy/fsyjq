<!--用于展示培训清单 -->
<template>
  <div id ='TrainingList'>
    <group>
        <cell title="培训一" value="value" link=""></cell>
        <cell title="培训二" value="value" link=""></cell>
        <cell title="培训三" value="value" link=""></cell>
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
  name: 'trainingList',
  components: { Group, Cell }
}
</script>

<style>

</style>