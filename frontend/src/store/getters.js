const getters = {
  sidebar: state => state.app.sidebar,
  token: state => state.user.token,
  username: state => state.user.username,
  email: state => state.user.email,
  cellphone: state => state.user.cellphone,
  last_login: state => state.user.last_login,
  is_admin: state => state.user.is_admin
}
export default getters
