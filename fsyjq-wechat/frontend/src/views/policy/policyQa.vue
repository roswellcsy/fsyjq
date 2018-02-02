<!--用于填写政策咨询,初版仅支持看自己的 -->
<template>
  <div id ='PolicyQa'>
    <group>
        <cell title="咨询人" value="value"></cell>
        <cell title="咨询时间" value="value"></cell>
        <cell title="标题" value="value"></cell>
        <cell title="内容" value="value"></cell>
        <cell title="答复" value="value"></cell>
        <cell title="答复时间" value="value"></cell>
      </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'policyQa',
  components: { Group, Cell }
}
</script>

<style>

</style>