<!--用于填写专业咨询问题及信息 -->
<template>
  <div id ='ProAdv'>
    <group>
        <cell title="姓名" value="value"></cell>
        <cell title="咨询问题标题" value="value"></cell>
        <cell title="咨询问题内容" value="value"></cell>
      </group>
  </div>
</template>

<script>
import { Group, Cell } from 'vux'
export default {
  name: 'ProAdv',
  components: { Group, Cell }
}
</script>

<style>

</style>