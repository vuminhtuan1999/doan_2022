import { createStore } from 'vuex'

export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
    curentUser: 0,
    student_code: '',
    isBooked: 0,
    rooms: [],
    bookingRoom: {},
    roomates: [],
    users: [],
    buildings: [],
    message : ''
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.curentUser = localStorage.getItem('user')
        state.student_code = localStorage.getItem('student_code')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.curentUser = {}
        state.student_code = ''
      }
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    setCurrentUser(state, user) {
      state.curentUser = user
    }, 
    removeCurrentUser(state) {
      state.curentUser = {}
    },
    setRooms(state, rooms) {
      state.rooms = rooms
    },
    removeRooms(state) {
      state.rooms = []
    },
    setBookingRoom(state, bookingRoom) {
      state.bookingRoom = bookingRoom
    },
    setRoomate(state, roomates){
      state.roomates = roomates
    },
    removeRoomate(state) {
      state.roomates = []
    },
    setUsers(state, users) {
      state.users = users
    },
    removUsers(state) {
      state.users = []
    },
    setBuildings(state, buildings) {
      state.buildings = buildings
    },
    removBuildings(state) {
      state.buildings = []
    },
    setIsBooked(state, isBooked) {
      state.isBooked = isBooked
    },
    setStudentCode(state, student_code) {
      state.student_code = student_code
    },
    setMessage(state, message) {
      state.message = message
    }
  },
  actions: {
  },
  modules: {
  }
})
