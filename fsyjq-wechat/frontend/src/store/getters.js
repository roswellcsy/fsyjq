const getters = {
  token: state => state.user.token,
  user_id: state => state.user.user_id,
  username: state => state.user.username,
  fullname: state => state.user.fullname,
  sex: state => state.user.sex,
  email: state => state.user.email,
  cellphone: state => state.user.cellphone,
  // last_login: state => state.user.last_login,
  // is_admin: state => state.user.is_admin,
  volornot: state => state.user.volornot
}
export default getters
