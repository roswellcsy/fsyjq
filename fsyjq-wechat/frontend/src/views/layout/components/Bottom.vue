<template>
  <div>
    <tabbar>
      <tabbar-item selected link="/policy">
        <img slot="icon" src="static/bottom/icon_nav_button.png">
        <span slot="label">政策相关</span>
      </tabbar-item>
      <tabbar-item selected link="/charitycampaign">
        <img slot="icon" src="static/bottom/icon_nav_msg.png">
        <span slot="label">公益活动</span>
      </tabbar-item>
      <tabbar-item selected link="/shareplatform">
        <img slot="icon" src="static/bottom/icon_nav_article.png">
        <span slot="label">共享平台</span>
      </tabbar-item>
      <tabbar-item selected link="/personal/userinfo">
        <img slot="icon" src="static/bottom/icon_nav_cell.png">
        <span slot="label">我的信息</span>
      </tabbar-item>
    </tabbar>
  </div>
</template>

<script>
  import { Tabbar, TabbarItem } from 'vux'

  export default {
    components: {
      Tabbar,
      TabbarItem
    }
  }
</script>
<style>

</style>
