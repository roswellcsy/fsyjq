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

