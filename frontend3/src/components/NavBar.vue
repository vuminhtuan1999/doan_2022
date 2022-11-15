<template>
  <!-- Sidebar  -->
    <nav id="sidebar">
        <div class="sidebar-header">
            <!-- <h3><img src="../../public/img/ktx1.jpg" class="img-fluid"/><span>{{this.user.username}}</span></h3> -->
            <h3><img src="../../public/img/ktx1.jpg" class="img-fluid"/><span>{{this.user.username}}</span></h3>

        </div>
        <ul class="list-unstyled components">
            <li  class="active">
                <router-link v-if="this.user.is_student" :to="{name: 'UserDashboard'}" class="dashboard"><i class="material-icons">dashboard</i><span>Trang chủ</span></router-link>
                <router-link v-else-if="this.user.is_admin" :to="{name: 'AdminDashboard'}" class="dashboard"><i class="material-icons">dashboard</i><span>Trang chủ</span></router-link>
            </li>
    
            <div class="small-screen navbar-display">
                <li class="dropdown">
                    <a href="#homeSubmenu0" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                        <i class="material-icons">notifications</i><span> 4 notification</span>
                    </a>
                    <ul class="collapse list-unstyled menu" id="homeSubmenu0">
                        <li>
                            <a v-if="this.user.is_student" href="#">You have 5 new messages</a>
                        </li>
                        <li>
                            <a v-if="this.user.is_student" href="#">You're now friend with Mike</a>
                        </li>
                        <li>
                            <a v-if="this.user.is_student" href="#">Wish Mary on her birthday!</a>
                        </li>
                        <li>
                            <a v-if="this.user.is_student" href="#">5 warnings in Server Console</a>
                        </li>
                    </ul>
                </li>
            
                <li  class="d-lg-none d-md-block d-xl-none d-sm-block">
                    <a href="#"><i class="material-icons">apps</i><span>apps</span></a>
                </li>
            
                <li  class="d-lg-none d-md-block d-xl-none d-sm-block">
                    <a href="#"><i class="material-icons">person</i><span>user</span></a>
                </li>
            
                <li  class="d-lg-none d-md-block d-xl-none d-sm-block">
                    <a href="#"><i class="material-icons">settings</i><span>setting</span></a>
                </li>
            </div>

            <!-- Quản lý tòa nhà  -->

            <li class="" v-if="this.user.is_admin">
                <router-link :to="{name: 'ListBuilding'}"><i class="material-icons">location_city</i><span>Quản Lý Tòa Nhà</span></router-link>
            </li>

            <!-- Quản lý đăng kí -->
        
            <li  v-if="this.user.is_student">   
                <a href="#homeSubmenu1" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle" id="dropdownMenuButton">
                    <i class="material-icons">home</i><span>Quản lý đăng ký</span>
                </a>
                <ul class="collapse" id="homeSubmenu1">
                    <li>
                        <router-link :to="{name: 'RoomRegistration'}" v-if="this.user.is_student">Đăng ký phòng</router-link>
                    </li>
                    <li>
                        <router-link :to="{name: 'BookingRoom'}" v-if="this.user.is_student">Xem đăng ký</router-link>
                    </li>
                    <li>
                        <router-link :to="{name: 'Roomate'}" v-if="this.user.is_student">Danh sách bạn cùng phòng</router-link>
                    </li>
                </ul>
               
                
            </li>

            <li class="" v-else-if="this.user.is_admin">
                <router-link :to="{name: 'ListBookingRoom'}"><i class="material-icons">event_note</i><span>Quản Lý Đăng Kí Phòng</span></router-link>
            </li>


            <!-- Dịch Vụ Hỗ Trợ -->
            
            <li class="dropdown">
                <a href="#pageSubmenu2" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                    <i class="material-icons">pin_drop</i><span>Dịch vụ hỗ trợ</span>
                </a>
                <ul class="collapse list-unstyled menu" id="pageSubmenu2">
                    <li>
                        <router-link v-if="this.user.is_student" :to="{name: 'LaundryService'}">Tiệm giặt là</router-link>
                        <!-- <router-link v-else-if="this.user.is_admin" :to="{name: 'LaundryService'}">Tiệm giặt là</router-link> -->
                    </li>
                    <li>
                        <router-link v-if="this.user.is_student" :to="{name: 'StudyRoomService'}">Phòng tự học chung</router-link>
                        <router-link v-else-if="this.user.is_admin" :to="{name: 'ListStudyRoom'}">Phòng tự học chung</router-link>
                    </li>
                </ul>
            </li>

            <!-- Hỗ Trợ Phản Ánh -->
            
            <li class="">
                <router-link v-if="this.user.is_student" :to="{name: 'Reflect'}"><i class="material-icons">event_note</i><span>Hỗ Trợ Phản Ánh</span></router-link>
                <router-link v-if="this.user.is_admin" :to="{name: 'ListReflect'}"><i class="material-icons">event_note</i><span>Hỗ Trợ Phản Ánh</span></router-link>
            </li>

            <!-- Cán Bộ -->

            <li class="dropdown">
                <router-link :to="{name: 'ListCadres'}" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                    <i class="material-icons">group</i><span>Cán bộ</span>
                </router-link>
                <ul class="collapse list-unstyled menu" id="pageSubmenu4">
                    <li>
                        <a href="#">Page 1</a>
                    </li>
                    <li>
                        <a href="#">Page 2</a>
                    </li>
                    <li>
                        <a href="#">Page 3</a>
                    </li>
                </ul>
            </li>


            
            <li class="dropdown">
                <a href="#pageSubmenu5" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                    <i class="material-icons">menu_book</i><span>Tài liệu học tập</span>
                </a>
                <ul class="collapse list-unstyled menu" id="pageSubmenu5">
                    <li>
                        <a href="#">Page 1</a>
                    </li>
                    <li>
                        <a href="#">Page 2</a>
                    </li>
                    <li>
                        <a href="#">Page 3</a>
                    </li>
                </ul>
            </li>
            
            
            
            <li class="dropdown">
                <a href="#pageSubmenu6" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                    <i class="material-icons">bookmark</i><span>Tài liệu chung</span>
                </a>
                <ul class="collapse list-unstyled menu" id="pageSubmenu6">
                    <li class="dropdown-item">
                        <a href="#">Page 1</a>
                    </li>
                    <li>
                        <a href="#">Page 2</a>
                    </li>
                    <li>
                        <a href="#">Page 3</a>
                    </li>
                </ul>
            </li>
            
            
            <li class="dropdown">
                <a href="#pageSubmenu7" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                    <i class="material-icons">payments</i><span>Thanh toán</span>
                </a>
                <ul class="collapse list-unstyled menu" id="pageSubmenu7">
                    <li>
                        <router-link v-if="this.user.is_student" :to="{name: 'PayLaundry'}">Hóa Đơn Giặt Là</router-link>
                        <router-link v-else-if="this.user.is_admin" :to="{name: 'ListPayLaundry'}">Hóa Đơn Giặt Là</router-link>
                    </li>
                    <li>
                        <router-link v-if="this.user.is_student" :to="{name: 'Payment'}">Hóa Đơn Tiền Phòng và Điện Nước</router-link>
                        <router-link v-else-if="this.user.is_admin" :to="{name: 'ListPayment'}">Hóa Đơn Tiền Phòng và Điện Nước</router-link>
                    </li>
                </ul>
            </li>
            
            <li class="">
                <a href="#"><i class="material-icons">event_note</i><span>Bảng ghi chú</span></a>
            </li>
            <li class="">
                <a href="#"><i class="material-icons">chat</i><span>Tin nhắn</span></a>
            </li>
                <li  class="">
                <router-link :to="{name : 'AccountInformation'}"><i class="material-icons">account_box</i><span>Tài khoản</span></router-link>
            </li>
        </ul>  
    </nav>
</template>

<script>
import axios from 'axios'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
export default {
    name: 'NavBar',
    data() {
        return {
            user: {},
            showMenu: false
        }
    },
    methods: {
        async getCurrentUser() {
            let token = this.$store.state.token
            console.log(123,this.$store)
            await axios.get(`/api/user/${this.$store.state.curentUser}/`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            }).then(resp => {
                this.user = resp.data
            }).catch(err => console.log(err))
        },
        // toggleShow: function() {
        //     console.log('duong', this.showMenu)
		// 	this.showMenu = !this.showMenu;
		// },
    },
    beforeCreate() {
        console.log('first',this.$store.state.curentUser)
        this.$store.commit('setCurrentUser', localStorage.getItem('user'))
    },
    mounted() {
        this.getCurrentUser()
    }
}
</script>

<style scoped>
    img {
        border-radius: 50%;
    }
    #sidebar {
        background-color: #1e1e2d;
        min-height: 707px;
    }
    #sidebar ul li a{
        color: #a2a3b7;
        font-size:12px;
    }
    #sidebar ul li a i{
        background-color: whitesmoke;
    }
    .sidebar-header{
        background-color: #1e1e2d !important;
    }
    .sidebar-header span{
        color: white;
    }
    .sidebar-header h3{
        text-transform: none;
        font-size: 15px;
    }
</style>