// import Cookies from 'js-cookie'

// const TokenKey = 'Admin-Token'

export function getToken() {
  // return Cookies.get(TokenKey)
  return window.localStorage.getItem('jwttoken')
}

export function setToken(jwttoken) {
  // return Cookies.set(TokenKey, token)
  return window.localStorage.setItem('jwttoken', jwttoken)
}

export function removeToken() {
  // return Cookies.remove(TokenKey)
  return window.localStorage.removeItem('jwttoken')
}

export function getUsername() {
  // return Cookies.get(TokenKey)
  return window.localStorage.getItem('username')
}

export function setUsername(username) {
  // return Cookies.set(TokenKey, token)
  return window.localStorage.setItem('username', username)
}

export function removeUsername() {
  // return Cookies.remove(TokenKey)
  return window.localStorage.removeItem('username')
}

export function setSex(user_information_sex) {
  // return Cookies.set(TokenKey, token)
  return window.localStorage.setItem('sex', user_information_sex)
}

export function setCellphone(user_information_cellphone) {
  // return Cookies.set(TokenKey, token)
  return window.localStorage.setItem('cellphone', user_information_cellphone)
}

export function setEmail(user_information_email) {
  // return Cookies.set(TokenKey, token)
  return window.localStorage.setItem('email', user_information_email)
}
