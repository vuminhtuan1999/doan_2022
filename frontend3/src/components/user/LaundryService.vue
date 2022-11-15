<template>
  <div class="wrapper to" id="wrapper">
    <!-- Slide bar -->
    <NavBar />

    <!-- Page content -->
    <div id="content">
      <div class="top-navbar">
        <Header />
      </div>

      <!-- Main content -->
      <div class="main-content">
        <h3 style="margin: 20px 0px">
          <i class="material-icons"> arrow_circle_right </i>
          Đăng ký phòng
        </h3>
        
        <div v-if="!this.error && this.message[0] !== '' && this.message[0] !== undefined">
            <div class="alert alert-success alert-dismissible fade show" role="alert" style="padding : 3px">
                <strong>Success!</strong> {{this.message[0]}}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        </div>

        <div v-if="this.error">
            <div v-for="(m, index) in this.message" :key="index" class="alert alert-danger alert-dismissible fade show" role="alert" style="padding : 3px">
                <strong>Error!</strong> {{m}}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        </div>

        <div>
            <p style="color: blue">Hạng thành viên : Mới</p>
            <p style="color: #00a65a">Quyền lợi : Hạng Bạc (giảm 10%), Hạng Vàng (giảm 15%), Hạng Kim Cương (giảm 20%)</p>
            <br>
            <table class="table table-bordered table-striped">
                <tbody>
                    <tr>
                        <td>Mã Thành Viên</td>
                        <td>Tên</td>
                        <td>Tổng định mức (kg)</td>
                        <td>Đã sử dụng (kg)</td>
                        <td>Còn lại</td>
                    </tr>

                    <tr>
                        <td>{{this.user.student_code}}</td>
                        <td>{{this.user.username}}</td>
                        <td></td>
                        <td style="color: #00a651"></td>
                        <td style="color: red">0</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div>
            <table class="table table-bordered table-striped">
                <thead>
                <tr>
                    <th>Gói</th>
                    <th>Giá (VNĐ)</th>
                    <th>Giới hạn người</th>
                    <th>Giới hạn giặt</th>
                    <th>Ưu đãi</th>
                    <th>Đăng kí</th>
                </tr>
                </thead>
                <tbody>
                    <tr v-for="type in this.type_laundrys" :key="type.id">
                        <td>{{type.type_name}}</td>
                        <td>{{type.cost}}</td>
                        <td>0</td>
                        <td>{{type.max_weight}} (kg)</td>
                        <td>{{type.note}}</td>
                        <td v-if="this.type !== 0">
                            <button v-if="this.type === type.id" class="btn btn-danger"  style="font-size: 12px !important" @click="deleteType(type.id)"> Hủy</button>
                            <button v-else class="btn btn-primary disabled" style="font-size: 12px !important" @click="getType(type.id)">Đăng Kí Gói</button>
                        </td>
                        <td v-else>
                            <button class="btn btn-primary" style="font-size: 12px !important" @click="getType(type.id)">Đăng Kí Gói</button>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p>THEO DÕI LỊCH SỬ</p>
        </div>

        <br>

        <div id="user-list-room_wrapperroom">
            <div class="dataTables_wrapper dt-bootstrap5 no-footer" id="table_export_wrapper">
                <div class="row">
                    <div class="col-sm-6">
                        <div class="dataTables_length" id="user-list-room_length">
                            <label for=""
                                >Show
                                <select @change="changePageSize($event)" name="" id="" class="form-select form-select-sm">
                                <option value="1" selected>1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="0">All</option>
                                </select>
                                Entries
                            </label>
                        </div>
                    </div>

                    <div class="col-sm-6">
                        <div id="user-list-room_filter" class="dataTables_filter">
                            <label for="">
                                Search:
                                <input type="search" v-model="query" @change="search($event)" class="form-control form-control-sm" />
                            </label>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-12">
                        <table
                        id="user-list-room"
                        class="table table-bordered table-striped datatable dataTable no-footer"
                        style="width: 100%"
                        >
                            <thead>
                                <tr role="row">
                                    <th>#</th>
                                    <th>Tên Phòng</th>
                                    <th>Đã đăng kí</th>
                                    <th>Đối tượng phòng kí túc xá</th>
                                    <th>Giá phòng trên tháng</th>
                                    <th>Đăng kí</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="odd">
                                    <th>#</th>
                                    <th>Tên Phòng</th>
                                    <th>Đã đăng kí</th>
                                    <th>Đối tượng phòng kí túc xá</th>
                                    <th>Giá phòng trên tháng</th>
                                    <th>Đăng kí</th>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-5">
                        <div id="user-list-room_info" class="dataTables_info">Showing 0 to 0 of 0 entries</div>
                    </div>

                    <div class="col-sm-7">
                        <div class="dataTables_paginate paging_simple_numbers" id="user-list-room_paginate">
                            <ul class="pagination">
                                <li class="paginate_button page-item previous" :class="{disabled : !showPreviousBtn}">
                                <button class="page-link" @click="goPrePage">Previoust</button>
                                </li>

                                <li class="page-item" v-for="(n, index) in number_page" :key="n" :class="{active : ((index + 1) === currentPage)}">
                                <button @click="choosePage(index + 1)" class="page-link">{{index + 1}}</button>
                                </li>

                                <li class="paginate_button page-item next" :class="{disabled : !showNextBtn}">
                                <button class="page-link" @click="goNextPage">Next</button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

            </div>
        </div>
        <!-- Footer -->
        <div class="footer-style">
          <Footer />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "../Header.vue";
import NavBar from "../NavBar.vue";
import Footer from "../Footer.vue";
import axios from 'axios'
export default {
    name: "LaundryService",
    components: {
        Header,
        NavBar,
        Footer,
    },
    data() {
        return {
            message: [],
            error: false,
            type_laundrys: [],
            type: 0,
            user: {},
            booking: {},
            page_size: 1,
            number_page: 0,
            count_of_data: 0,
            showNextBtn: false,
            showPreviousBtn: false,
            currentPage: 1,
            query: ''
        }
    },
    methods: {
        getType(typeID) {
            this.error = false
            this.message = []
            let token = this.$store.state.token

            let formData = {
                user: this.user.id,
                type: typeID
            }

            axios.post(`/api/booking-service/`, formData, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            }).then(resp => {
                this.message.push("Your request is Successfully")
                this.error = false
                this.getBooking()
                this.getListTypeLaudry()
            }).catch(err => {
                this.message = Object.values(err.response.data)
                this.error = true
            })
        },
        deleteType(typeID) {
            this.error = false
            this.message = []
            let token = this.$store.state.token
            axios.delete(`/api/booking-service/${this.booking.id}/`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            }).then(resp => {
                this.message.push("Delete Successfully!!!")
                this.error = false
                this.type = 0
                this.getListTypeLaudry()
            }).catch(err => {
                this.message = Object.values(err.response.data)
                this.error = true
            })
        },
        async getListTypeLaudry() {
            let token = this.$store.state.token

            await axios.get(`/api/type-laundry/`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            }).then(resp => {
                this.type_laundrys = resp.data
            }).catch(err => console.log(err))
        },
        async getUser() {
            let token = this.$store.state.token

            await axios.get(`/api/user/${localStorage.getItem('user')}/`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            }).then(resp => {
                this.user = resp.data
            }).catch(err => console.log(err))
        },
        async getBooking() {
            let token = this.$store.state.token

            await axios.get(`/api/booking-service/?size=0`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            }).then(resp => {
                this.booking = resp.data.find(el => el.user === this.user.id)
                if (this.booking) this.type = this.booking.type
            }).catch(err => console.log(err))
        }
    },
    mounted() {
        this.getListTypeLaudry()
        this.getUser()
        this.getBooking()
    }
}
</script>

<style scoped>
#user-list-room_wrapperroom {
  margin-top: 20px;
  margin-bottom: 20px;
  box-shadow: 0 0 20px rgb(0 0 0 / 11%);
  background-color: #ffffff;
  padding: 30px;
  border-radius: 5px;
}
#user-list-room {
  padding: 30px 0px;
}
.btn-action {
  width: 150px;
  border-radius: 50px;
  border: none;
  background: rgb(123, 97, 226);
}
.main-content {
  background-color: #f2f3f8;
  font-family: "Helvetica Neue", Helvetica, "Noto Sans", sans-serif, Arial,
    sans-serif;
font-size: 12px;
}
table.table-bordered.dataTable th,
table.table-bordered.dataTable td {
  font-size: 12px;
  text-align: left;
  vertical-align: middle;
}
table.table-bordered.dataTable th {
  font-family: "Helvetica Neue", Helvetica, "Noto Sans", sans-serif, Arial,
    sans-serif;
  font-weight: 550;
}
.btn-info {
  background-color: #42a5f5 !important;
  color: #ffffff;
  border-radius: 5px;
}
h3 {
  font-size: 22px;
}
.material-icons {
  font-family: "Material Icons";
  font-weight: normal;
  font-style: normal;
  font-size: 20px !important; /* Preferred icon size */
  display: inline-block;
  line-height: 1;
  text-transform: none;
  letter-spacing: normal;
  word-wrap: normal;
  white-space: nowrap;
  direction: ltr;
  /* Support for all WebKit browsers. */
  -webkit-font-smoothing: antialiased;
  /* Support for Safari and Chrome. */
  text-rendering: optimizeLegibility;
  /* Support for Firefox. */
  -moz-osx-font-smoothing: grayscale;
  /* Support for IE. */
  font-feature-settings: "liga";
}
</style>