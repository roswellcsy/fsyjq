import { login, getInfo } from '@/api/login'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { setUsername } from '@/utils/auth'

const user = {
  state: {
    token: getToken(),
    username: '',
    // email: '',
    // cellphone: '',
    last_login: '',
    is_admin: ''
    // avatar: '',
    // roles: []
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_USERNAME: (state, username) => { // 自定义修改
      state.username = username
    },
    SET_LL: (state, last_login) => { // 自定义修改
      state.last_login = last_login
    },
    SET_ISADMIN: (state, is_admin) => { // 自定义修改
      state.is_admin = is_admin
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
          setToken(jwttoken)
          setUsername(username)
          commit('SET_TOKEN', localStorage.jwttoken)
          commit('SET_USERNAME', localStorage.username) // 登录后先设好用户名，接下来在获取用户信息会用到
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
    // 获取用户信息
    GetInfo({ commit, state }) {
      return new Promise((resolve, reject) => {
        getInfo(localStorage.username, localStorage.token).then(response => {
          const r = response
          // commit('SET_USERNAME', r.username)
          commit('SET_LL', r.last_login)
          commit('SET_ISADMIN', r.is_admin)
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
        // commit('SET_TOKEN', '')
        removeToken()
        resolve()
      })
    }
  }
}

export default user
