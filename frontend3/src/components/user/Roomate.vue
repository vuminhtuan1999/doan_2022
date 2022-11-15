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
        <div id="user-list-room_wrapperroom">
          <div
            id="user-list-room_wrapper"
            class="dataTables_wrapper dt-bootstrap5 no-footer"
          >
            <div class="row">
              <div class="col-sm-12 col-md-6">
                <div class="dataTables_length" id="user-list-room_length">
                  <label for=""
                    >Show
                    <select @change="changePageSize($event)" name="" id="" class="form-select form-select-sm">
                      <option value="0" selected>All</option>
                    </select>
                    Entries
                  </label>
                </div>
              </div>

              <!-- <div class="col-sm-12 col-md-6">
                <div id="user-list-room_filter" class="dataTables_filter">
                  <label for="">
                    Search:
                    <input type="search" v-model="query" @change="search($event)" class="form-control form-control-sm" />
                  </label>
                </div>
              </div> -->
            </div>
          

            <div class="row">
              <div class="col-sm-12">
                <table
                  id="user-list-room"
                  class="table table-bordered dataTable no-footer"
                  style="width: 100%"
                >
                  <thead>
                    <tr>
                        <th>#</th>
                        <th>Username</th>
                        <th>Khóa</th>
                        <th>Mã Số Sinh Viên</th>
                        <th>Ghi chú</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="rm in roomates" :key="rm.id">
                        <td>{{rm.id}}</td>
                        <td>{{rm.username}}</td>
                        <td>{{rm.course_year}}</td>
                        <td>{{rm.student_code}}</td>
                        <td>Tài khoản đã active</td>
                    </tr>
                  </tbody>

                  <tfoot>
                    <tr>
                        <th>#</th>
                        <th>Username</th>
                        <th>Khóa</th>
                        <th>Mã Số Sinh Viên</th>
                        <th>Ghi chú</th>
                    </tr>
                  </tfoot>
                </table>
              </div>
            </div>

            <div class="row">
              <div class="col-sm-12 col-md-5">
                <div id="user-list-room_info" class="dataTables_info">Showing 0 to 0 of 0 entries</div>
              </div>

              <div class="col-sm-12 col-md-7">
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
import axios from 'axios'
import Header from '../Header.vue'
import NavBar from '../NavBar.vue'
import Footer from '../Footer.vue'
export default {
    name: 'Roomate',
    components: {
        Header,
        NavBar,
        Footer
    },
    data() {
        return{
            roomates: [],
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
        getNumberPage() {
            this.number_page = (this.count_of_data % this.page_size === 0) ? (this.count_of_data / this.page_size) : (parseInt(this.count_of_data / this.page_size) + 1)
        },
        async getRoomate() {
            this.number_page = 1
            var token = this.$store.state.token
            var id = this.$store.state.bookingRoom.room

            await axios.get(`/api/room-user-list/${id}/`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            })
            .then(resp => {
                this.roomates = resp.data
            }).catch(err => console.log(err))
                
        }
    },
    beforeCreate() {
        this.$store.commit("setBookingRoom", JSON.parse(localStorage.getItem('bookingRoom')))
    },
    mounted() {
        this.getRoomate()
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