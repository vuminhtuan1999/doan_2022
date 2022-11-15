import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home'
import SignUp from '../components/SignUp'
import Login from '../components/Login'
import AccountInformation from '../components/AccountInformation'
import Notification from '../components/Notification'
import NotPermission from '../components/NotPermission'

//Import Admin
import AdminHome from '../components/admin/AdminHome'
import AdminDashboard from '../components/admin/AdminDashboard'
import Rooms from '../components/admin/ListRoom'
import Users from '../components/admin/ListUser'
import Buildings from '../components/admin/ListBuilding'
import ListBookingRoom from '../components/admin/ListBookingRoom'
import ListStudyRoom from '../components/admin/ListStudyRoom'
import ListReflect from '../components/admin/ListReflect'
import ListPayLaundry from '../components/admin/ListPayLaundry'
import ListPayment from '../components/admin/ListPayment'

//Import User
import UserHome from '../components/user/UserHome'
import UserDashboard from '../components/user/UserDashBoard'
import ListRoom from '../components/user/ListRoom'
import BookingRoom from '../components/user/BookingRoom'
import Roomate from '../components/user/Roomate'
import ListCadres from '../components/user/ListCadres'
import LaundryService from '../components/user/LaundryService'
import Reflect from '../components/user/Reflect'
import StudyRoom from '../components/user/StudyRoomService'
import Payment from '../components/user/Payment'
import PayLaundry from '../components/user/PayLaundry'

//Import Store
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/notification',
    name: 'Notification',
    component: Notification
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/person/account-information',
    component : AccountInformation,
    name: 'AccountInformation',
    // meta: {
    //   requireAuth: true
    // }
  },
  {
    path: '/admin',
    component: AdminHome,
    // meta: {
    //   requireAuth: true
    // },
    children: [
      {
        path: '',
        name: 'AdminDashboard',
        component: AdminDashboard
      },
      {
        path: 'users',
        name: 'ListUser',
        component: Users
      },
      {
        path: 'buildings',
        name: 'ListBuilding',
        component: Buildings
      },
      {
        path: 'buildings/:id/rooms',
        name: 'ListRoom',
        component: Rooms
      },
      {
        path: 'booking-room',
        name: 'ListBookingRoom',
        component: ListBookingRoom
      },
      {
        path: 'stydy-rooms',
        name: 'ListStudyRoom',
        component: ListStudyRoom
      },
      {
        path: 'reflects',
        name: 'ListReflect',
        component: ListReflect
      },
      {
        path: 'list-payment-laundry',
        name: 'ListPayLaundry',
        component: ListPayLaundry
      }, 
      {
        path: 'payments',
        name: 'ListPayment',
        component: ListPayment
      }
    ]
  },
  {
    path: '/user',
    component: UserHome,
    // meta: {
    //   requireAuth: true
    // },
    children: [
      {
        path: '',
        name: 'UserDashboard',
        component: UserDashboard
      },
      {
        path: 'room-registration',
        name: 'RoomRegistration',
        component: ListRoom
      },
      {
        path: 'booking-room',
        name: 'BookingRoom',
        component: BookingRoom
      },
      {
        path: 'roomate',
        name: 'Roomate',
        component: Roomate
      },
      {
        path: 'list-cadres',
        name: 'ListCadres',
        component: ListCadres
      },
      {
        path: 'laundry-service',
        name: 'LaundryService',
        component: LaundryService
      },
      {
        path: 'studyroom-service',
        name: 'StudyRoomService',
        component: StudyRoom
      },
      {
        path: 'reflect',
        name: 'Reflect',
        component: Reflect
      },
      {
        path: 'payment',
        name: 'Payment',
        component: Payment
      },
      {
        path: 'payment-laundry',
        name: 'PayLaundry',
        component: PayLaundry
      }
    ]
  },
  {
    path: '/not-permission',
    name: 'NotPermission',
    component: NotPermission
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from , next) => {
  if (to.matched.some(record => record.meta.requireAuth) && !store.state.isAuthenticated) {
    next({name: 'NotPermission', query: {to: to.path} });
  } else {
    next()
  }
})

export default router
