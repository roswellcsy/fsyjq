<!--用于展示我的公益活动清单 -->

<template>
  <div id ='MyCampaignList'>
    <!-- <group> -->
    <!-- 根据后端获取到的发布活动列表，动态生成公益活动清单 -->
    <group>
      <template v-for="list in lists">
          <cell :title=list.campaign_name :value=list.campaign_date @click.native.prevent="setCurrenttitle($event)" link="/personal/userCampaign"></cell>
      </template>
    </group>
    <template>
      <group style="padding:5px 20px;">
        <x-button type="primary" action-type="button" link="/campaign/list">公益活动清单</x-button>
      </group>
    </template>
  </div>
</template>

<script>
import { fetchMylist } from '@/api/campaign'
import { Group, Cell, FormPreview, XButton } from 'vux'
// import { METHODS } from 'http';
export default {
  name: 'mycampaignlist',
  components: { Group, Cell, FormPreview, XButton },
  data() { // data()需要跟return
    return {
      lists: this.lists
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      fetchMylist(window.localStorage.getItem('username')).then(response => {
        this.lists = response
        window.localStorage.setItem('mycampaignlists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
    },
    setCurrenttitle() {
      const el = event.currentTarget
      window.localStorage.setItem('clicktitle', el.innerText.split('\n')[0])
    }
  }
}
</script>

<style>

</style>