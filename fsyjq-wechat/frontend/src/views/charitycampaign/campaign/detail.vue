<!--用于展示公益活动详细信息 -->
<!-- 需要动态从后台读取轮播图片，待处理 -->
<template>
  <div id ='CampaignDetail'>
    <!-- <group-title>自动轮播</group-title> -->
    <swiper :list=demo03_list auto style="width:100%;margin:0 auto;" height="180px" dots-class="custom-bottom" dots-position="center"></swiper>
    <group>
        <cell title='活动名称:' :value=content[0].campaign_name></cell>
        <cell title='活动分类:' :value=content[0].campaign_type></cell>
        <datetime title='活动时间:' :value=content[0].campaign_date :readonly=True></datetime>
        <datetime title='报名截止:' :value=content[0].campaign_signup_deadline :readonly=True></datetime>
        <cell title='服务对象:' :value=content[0].campaign_client></cell>
        <cell title='活动地点:' :value=content[0].campaign_address></cell>
        <cell title='活动内容:' :value=content[0].campaign_content></cell>
        <cell title='服务费用:' :value=content[0].campaign_paid></cell>
        <cell title='联系方式:' :value=content[0].campaign_contact></cell>
        <cell title='活动认证时数:' :value=content[0].campaign_certified_hours></cell>
        <cell title='可报名参与人数:' :value=content[0].campaign_counts></cell>
        <cell title='可报名志愿者人数:' :value=content[0].campaign_vol_counts></cell> 
    </group>
    <group>
      <span>活动后台ID：{{ content[0].id }}</span>
    </group>
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleSignup">报名</x-button>
    </group>
    <group>
      <cell>活动报名</cell>
    </group>

  </div>
</template>

<script>
import { fetchCurrentcampaign, campaignSignup } from '@/api/campaign'
import { Swiper, Group, Cell, Datetime, XButton } from 'vux'

const imgList = [
  'http://placeholder.qiniudn.com/800x300/FF3B3B/ffffff',
  'http://placeholder.qiniudn.com/800x300/FFEF7D/ffffff',
  'http://placeholder.qiniudn.com/800x300/8AEEB1/ffffff',
  'http://localhost:8000/media/media/IMG_6061_6gUn15p.JPG'
]
// const imgList = []

// for (link in content[0].photos) {
//   imgList.push(link.photo_path)
// }
// const demoList = []
const demoList = imgList.map((one, index) => ({
  url: 'javascript:',
  img: one
}))

export default {
  name: 'campaignDetail',
  components: { Swiper, Group, Cell, Datetime, XButton },
  // const imgList : new Array(),
  data() {
    return {
      // imgList: this.imgList,
      demo03_list: demoList,
      // demo_list: this.demoList1,
      content: this.content
    }
  },
  // computed: {
  //   fetchImagelist: function() {
  //     const imgList = []
  //     for (this.img in this.content[0].photos) {
  //       imgList.push(this.img)
  //     }
  //     // const demoList1 = imgList.map((one, index) => ({
  //     //   url: 'javascript:',
  //     //   img: one
  //     // }))
  //     return imgList
  //   }
  // },
  // mounted() {

  // },
  created() {
    this.fetchData()
    // this.fetchImagelist()
  },
  methods: {
    fetchData() {
      fetchCurrentcampaign(window.localStorage.getItem('clicktitle')).then(response => {
        this.content = response
        // window.localStorage.setItem('campaignlists', this.lists)
      }).catch(err => {
        // this.fetchSuccess = false
        console.log(err)
      })
    },
    // fetchImagelist() {
    //   const imgList = []
    //   for (this.img in this.content[0].photos) {
    //     imgList.push(this.img)
    //   }
    //   // const demoList1 = imgList.map((one, index) => ({
    //   //   url: 'javascript:',
    //   //   img: one
    //   // }))
    //   return imgList
    // }
    handleSignup() {
      console.log('点击报名')
      campaignSignup(this.content[0].id, window.localStorage.getItem('user_id')).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
        this.$router.push({ path: '/campaign/list' })
      }).catch(error => {
        console.log(error)
        // reject(error)
      })
    }
  }
}
</script>

<style>

</style>