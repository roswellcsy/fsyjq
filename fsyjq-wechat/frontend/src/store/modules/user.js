import { login, getInfo, getDetailinfo } from '@/api/login'
import { getVolinfo } from '@/api/volunteer'
import { getToken, removeToken } from '@/utils/auth'

const user = {
  state: {
    token: getToken(),
    username: '',
    fullname: '',
    sex: '',
    email: '',
    cellphone: '',
    // volornot: '',
    // last_login: '',
    // is_admin: '',
    user_id: ''
    // avatar: '',
    // roles: []
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
      window.localStorage.setItem('jwttoken', token)
    },
    SET_USERNAME: (state, username) => { // 自定义修改
      state.username = username
      window.localStorage.setItem('username', username)
    },
    SET_FULLNAME: (state, fullname) => { // 自定义修改
      state.fullname = fullname
      window.localStorage.setItem('fullname', fullname)
    },
    // SET_LL: (state, last_login) => { // 自定义修改
    //   state.last_login = last_login
    //   window.localStorage.setItem('last_login', last_login)
    // },
    // SET_ISADMIN: (state, is_admin) => { // 自定义修改
    //   state.is_admin = is_admin
    //   window.localStorage.setItem('is_admin', is_admin)
    // },
    SET_SEX: (state, sex) => {
      state.sex = sex
      window.localStorage.setItem('sex', sex)
    },
    SET_CELLPHONE: (state, cellphone) => {
      state.cellphone = cellphone
      window.localStorage.setItem('cellphone', cellphone)
    },
    SET_EMAIL: (state, email) => {
      state.email = email
      window.localStorage.setItem('email', email)
    },
    // SET_VOLORNOT: (state, volornot) => {
    //   state.volornot = volornot
    //   window.localStorage.setItem('volornot', volornot)
    // },
    SET_USERID: (state, user_id) => {
      state.user_id = user_id
      window.localStorage.setItem('user_id', user_id)
    },
    SET_USERINFOID: (state, user_info_id) => {
      state.user_info_id = user_info_id
      window.localStorage.setItem('user_info_id', user_info_id)
    },
    SET_VOLINFOID: (state, vol_info_id) => {
      state.vol_info_id = vol_info_id
      window.localStorage.setItem('vol_info_id', vol_info_id)
    }
    // SET_AVATAR: (state, avatar) => {
    //   state.avatar = avatar
    // },
    // SET_ROLES: (state, roles) => {
    //   state.roles = roles
    // }
  },

  actions: {
    // 登录
    Login({ commit }, userInfo) {
      const username = userInfo.username.trim()
      return new Promise((resolve, reject) => {
        login(username, userInfo.password).then(response => { // mockserver返回20000和包在data的token，实际后端只返回token
          const jwttoken = response.token
          // localStorage.jwttoken = response.token
          // localStorage.username = username
          // setToken(jwttoken)
          // setUsername(username)
          commit('SET_TOKEN', jwttoken)
          commit('SET_USERNAME', username) // 登录后先设好用户名，接下来在获取用户信息会用到
          // commit('SET_USERID', id)
          // const jwttoken = response.token
          // console.log(jwttoken)
          // setToken(jwttoken)
          // commit('SET_TOKEN', jwttoken)
          resolve()
        }).catch(error => {
          console.log(error)
          reject(error)
        })
      })
    },
    // 获取账号基本信息
    GetInfo({ commit, state }) {
      return new Promise((resolve, reject) => {
        getInfo(localStorage.username).then(response => {
          const r = response[0]
          commit('SET_USERNAME', localStorage.username)
          // commit('SET_LL', r.user_information_user.last_login)
          // commit('SET_ISADMIN', r.user_information_user.is_admin)
          // commit('SET_FULLNAME', r.user_information_name)
          // commit('SET_SEX', r.user_information_sex)
          // commit('SET_CELLPHONE', r.user_information_cellphone)
          // commit('SET_EMAIL', r.user_information_email)
          // commit('SET_VOLORNOT', r.user_information_volunteer)
          commit('SET_USERID', r.id)
          resolve(response)
        }).catch(error => {
          reject(error)
        })
      })
    },
    GetDetailInfo({ commit, state }) {
      return new Promise((resolve, reject) => {
        getDetailinfo(localStorage.username).then(response => {
          const r = response[0]
          // commit('SET_USERNAME', localStorage.username)
          // commit('SET_LL', r.user_information_user.last_login)
          // commit('SET_ISADMIN', r.user_information_user.is_admin)
          commit('SET_FULLNAME', r.user_information_name)
          commit('SET_SEX', r.user_information_sex)
          commit('SET_CELLPHONE', r.user_information_cellphone)
          commit('SET_EMAIL', r.user_information_email)
          // commit('SET_VOLORNOT', r.user_information_volunteer)
          commit('SET_USERINFOID', r.id)
          resolve(response)
        }).catch(error => {
          reject(error)
        })
      })
    },
    GetVolInfo({ commit, state }) {
      return new Promise((resolve, reject) => {
        getVolinfo(localStorage.username).then(response => {
          const r = response[0]
          // commit('SET_USERNAME', localStorage.username)
          // commit('SET_LL', r.user_information_user.last_login)
          // commit('SET_ISADMIN', r.user_information_user.is_admin)
          commit('SET_VOLINFOID', r.id)
          resolve(response)
        }).catch(error => {
          reject(error)
        })
      })
    },
    // 登出,当前只有前端登出，后期完善
    // LogOut({ commit, state }) {
    //   return new Promise((resolve, reject) => {
    //     logout(state.token).then(() => {
    //       commit('SET_TOKEN', '')
    //       commit('SET_ROLES', [])
    //       removeToken()
    //       resolve()
    //     }).catch(error => {
    //       reject(error)
    //     })
    //   })
    // },

    // 前端 登出
    FedLogOut({ commit }) {
      return new Promise(resolve => {
        commit('SET_USERID', '')
        removeToken()
        // window.localStorage.clear()
        resolve()
      })
    }
  }
}

export default user
