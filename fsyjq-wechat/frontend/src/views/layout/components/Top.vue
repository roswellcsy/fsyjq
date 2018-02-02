<!--
头部操作栏，回退上一页可以使用this.$router.go(-1)
{{title}}
加上从每个appmain回传的title
-->
<template>
  <div id="Top">
    <x-header slot="header" style="width:100%;relative:absolute;left:0;top:0;z-index:100;"
              :left-options="{showBack: true, backText: '返回'}" 
              :right-options="{showMore: false}"
              @on-click-more="showMenus = false">禅城区幸福一家亲
    </x-header>

    <!-- <x-header :right-options="{showMore: true}" @on-click-more="showMenus = true">with more menu</x-header> -->
    <!-- <div v-transfer-dom>
      <popup v-model="showMenus" position="right">
        <div style="width:200px;">
          <group>
            <cell @click.native="handleFedLogOut">登出</cell>
            <x-button type="primary" action-type="button" @click.native.prevent="handleFedLogOut">登出</x-button>
          </group>
        </div>
      </popup>
    </div> -->
    <!-- <p>test</p> -->
  </div>
</template>

<script>
  // import { mapState } from 'vuex'
  import { XHeader, TransferDom, Popup, Group, Cell, XButton } from 'vux'

  export default {
    directives: {
      TransferDom
    },
    components: {
      XHeader,
      Popup,
      Group,
      Cell,
      XButton
    },
    // computed: {
    //   ...mapState({
    //     showBack: state => state.vux.showBack,
    //     title: state => state.vux.title
    //   })
    // },
    data() {
      return {
        // menuList: [
        //   { title: 'userInfo', value: '', url: '/userInfo' },
        //   { title: '', value: 'userInfo', url: '/userInfo', class: 'menu' },
        //   { title: 'userInfo', value: '', url: '/userInfo' },
        //   { title: '', value: 'userInfo', url: '/userInfo', class: 'menu' }
        // ],
        showMenus: false
      }
    },
    methods: {
      // goToUrl(path) {
      //   if (path) {
      //     console.log(path)
      //   }
      //   // let vue = this
      // }
      handleFedLogOut() { // 登出
        this.$store.dispatch('FedLogOut').then(() => {
          // this.loading = false
          this.$router.push({ path: '/' })
        }).catch(() => {
          // this.loading = false
          console.log('something wrong')
        })
      }
    }
  }
</script>
<style>
  *{font-size: 14px}
  #Top .vux-header-title {
    font-size: 16px;
  }
  #Top .menu {
    margin-right: 70px;
  }
  #Top .menu div {
    color: #000;
  }
  #Top .menu:before {
    right: -70px;
  }
</style>
