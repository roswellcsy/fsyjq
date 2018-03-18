<!--用于展示培训详情及报名 -->
<!-- 需要动态从后台读取轮播图片，待处理 -->
<template>
  <div id ='TrainingDetail'>
    <!-- <group-title>自动轮播</group-title> -->
    <swiper :list=demo03_list auto style="width:100%;margin:0 auto;" height="180px" dots-class="custom-bottom" dots-position="center"></swiper>
    <group>
        <cell title='主讲人:' :value=content[0].at_zhu_jiang_ren></cell>
        <cell title='培训主题:' :value=content[0].at_theme></cell>
        <datetime title='培训日期:' :value=content[0].at_date :readonly=True></datetime>
        <datetime title='报名截止日期:' :value=content[0].at_sign_up_deadline :readonly=True></datetime>
        <cell title='培训内容:' :value=content[0].at_content></cell>
        <cell title='培训地址:' :value=content[0].at_address></cell>
        <cell title='培训可报名人数:' :value=content[0].at_counts></cell>
        
    </group>
    <group style="padding:5px 20px;">
      <x-button type="primary" action-type="button" @click.native.prevent="handleSignup">报名</x-button>
    </group>

  </div>
</template>

<script>
import { fetchCurrentTraining, TrainingSignup } from '@/api/volunteer'
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
  name: 'trainingDetail',
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
      fetchCurrentTraining(window.localStorage.getItem('clicktrainingtitle')).then(response => {
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
      TrainingSignup(this.content[0].id, window.localStorage.getItem('user_id')).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
        this.$router.push({ path: '/personal/userTraininglist' })
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