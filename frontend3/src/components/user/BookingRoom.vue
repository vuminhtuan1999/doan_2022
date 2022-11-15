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
        <div v-if="!this.error && this.message[0] !== ''" class="alert alert-success alert-dismissible fade show" role="alert" style="padding : 3px">
                    <strong>Success!</strong> {{this.message[0]}}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
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
                    <select
                      @change="changePageSize($event)"
                      name=""
                      id=""
                      class="form-select form-select-sm"
                    >
                      <option value="1" selected>1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="0">All</option>
                    </select>
                    Entries
                  </label>
                </div>
              </div>

              <div class="col-sm-12 col-md-6">
                <div id="user-list-room_filter" class="dataTables_filter">
                  <label for="">
                    Search:
                    <input
                      type="search"
                      v-model="query"
                      @change="search($event)"
                      class="form-control form-control-sm"
                    />
                  </label>
                </div>
              </div>
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
                      <th>Tên Kí Túc Xá</th>
                      <th>Phòng Đã Đăng Kí</th>
                      <th>Kì Đăng Kí</th>
                      <th>Ngày Đăng Kí</th>
                      <th>Ngày Xác Nhận</th>
                      <th>Trạng Thái Yêu Cầu</th>
                      <th>Loại</th>
                      <th>In Đơn Đăng Kí</th>
                      <th>Lựa Chọn</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-if="this.isBooked === 1">
                        <td>KTX Thủy Lợi</td>
                        <td>{{ this.bookingRoom.room_name }}</td>
                        <td>{{ getCourse() }}</td>
                        <td style="width=20px !important">{{ getBookedDate(bookedDate) }}</td>
                        <td></td>
                        <td>
                        <p class="message">
                            Đăng kí thành công, SV thanh toán theo hướng dẫn
                        </p>
                        </td>
                        <td>SV ngoại trú đăng kí</td>
                        <td>
                        <button class="btn btn-primary print"  @click="print()">
                            <i class="material-icons">print</i>
                            In
                        </button>
                        </td>
                        <td>
                        <button class="btn btn-primary delete" @click="removeBooking()">
                            <i class="material-icons">check</i>
                            Xóa
                        </button>
                        </td>
                    </tr>
                    <tr v-else>
                        <div class="align-middle">No data</div>
                    </tr>
                  </tbody>

                  <tfoot>
                    <tr>
                      <th>Tên Kí Túc Xá</th>
                      <th>Phòng Đã Đăng Kí</th>
                      <th>Kì Đăng Kí</th>
                      <th>Ngày Đăng Kí</th>
                      <th>Ngày Xác Nhận</th>
                      <th>Trạng Thái Yêu Cầu</th>
                      <th>Loại</th>
                      <th>In Đơn Đăng Kí</th>
                      <th>Lựa Chọn</th>
                    </tr>
                  </tfoot>
                </table>
              </div>
            </div>

            <div class="row">
              <div class="col-sm-12 col-md-5">
                <div id="user-list-room_info" class="dataTables_info">
                  Showing 0 to 0 of 0 entries
                </div>
              </div>

              <div class="col-sm-12 col-md-7">
                <div
                  class="dataTables_paginate paging_simple_numbers"
                  id="user-list-room_paginate"
                >
                  <ul class="pagination">
                    <li
                      class="paginate_button page-item previous"
                      :class="{ disabled: !showPreviousBtn }"
                    >
                      <button class="page-link" @click="goPrePage">
                        Previoust
                      </button>
                    </li>

                    <li
                      class="page-item"
                      v-for="(n, index) in number_page"
                      :key="n"
                      :class="{ active: index + 1 === currentPage }"
                    >
                      <button @click="choosePage(index + 1)" class="page-link">
                        {{ index + 1 }}
                      </button>
                    </li>

                    <li
                      class="paginate_button page-item next"
                      :class="{ disabled: !showNextBtn }"
                    >
                      <button class="page-link" @click="goNextPage">
                        Next
                      </button>
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
import axios from "axios";
import $ from "jquery";
import Header from "../Header.vue";
import NavBar from "../NavBar.vue";
import Footer from "../Footer.vue";
export default {
  name: "BookingRoom",
  components: {
    Header,
    NavBar,
    Footer,
  },
  data() {
    return {
      message : [],
      error : false,
      isBooked: 0,
      bookingRoom: {},
      bookedDate: null,
      page_size: 1,
      number_page: 0,
      count_of_data: 0,
      showNextBtn: false,
      showPreviousBtn: false,
      currentPage: 1,
      query: ''
    };
  },
  methods: {
    getNumberPage() {
      this.number_page = (this.count_of_data % this.page_size === 0) ? (this.count_of_data / this.page_size) : (parseInt(this.count_of_data / this.page_size) + 1)
    },
    goNextPage() {
      this.currentPage += 1
      this.getListRoom()
    },
    goPrePage() {
      this.currentPage -= 1
      this.getListRoom()
    },
    choosePage(i) {
      this.currentPage = i
      this.getListRoom()
    },
    changePageSize(e) {
      this.page_size = parseInt(e.target.value)
      this.number_page = 0
      this.getListRoom()
    },
    search(e) {
      this.query = e.target.value
      if (this.query !== '') {
        this.getListRoom()
      }
      this.getListRoom()
    },

    getCourse() {
      var today = new Date();
      var course1 = [9, 10, 11, 12, 1];
      var course2 = [2, 3, 4, 5, 6];
      var course3 = [7, 8];
      var course = "";
      if (course1.includes(today.getMonth() + 1)) course = "1";
      else if (course2.includes(today.getMonth() + 1)) course = "2";
      else course = "3";
      return today.getFullYear() + course;
    },

    getBookedDate(date) {
      var day = new Date(date);
      return day;
    },
    print(){
      let printme = document.getElementById('user-list-room')
      let we = window.open("", "", "width: 900, height: 700");
      we.document.write(printme.outerHTML)
      we.document.close()
      we.focus()
      we.print()
      we.close()
    },
    removeBooking(){
      let token = this.$store.state.token
      let booking = this.$store.state.bookingRoom
      axios.delete(`/api/booking-room/${booking.id}/`,{
        headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
      }).then(resp => {
        console.log('Delete Success!')
        this.getisBooked()
      }).catch(err => 
        console.log(err)
      )
    },
    async getisBooked() {
      var token = this.$store.state.token
      var currentUserID = parseInt( this.$store.state.curentUser )
      await axios.get('/api/booking-room/', {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
      }).then(resp => {
            var bookings = resp.data
            var check1 = false
            bookings.forEach(element => {
              if(element.user === currentUserID) {
                check1 = true
                localStorage.setItem('bookingRoom', JSON.stringify(element))
              }
            });
            if (check1) this.isBooked = 1
            else this.isBooked = 0 
            console.log(this.isBooked);
            localStorage.setItem('isBooked', this.isBooked)
            if (this.isBooked === 1) {
              console.log("sfasfa");
              this.getData()
            }

            //Check user đã có phòng chưa
            if (this.isBooked === 0) {
              axios.get('/api/room-user/', {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
                }).then(resp => {
                      var room_users = resp.data
                      var check = false
                      room_users.forEach(element => {
                        if(element.user === currentUserID) {
                          check = true
                        } 
                      });
                      if (check) this.isBooked = 2
                      else this.isBooked = 0 

                      localStorage.setItem('isBooked', this.isBooked)
                }).catch(err => console.log(err))
            }
            
      }).catch(err => console.log(err))
    },
    async getData() {
      this.number_page = 1
      var token = this.$store.state.token
        
      await axios.get(`/api/room/?size=0`, {
          headers: {
              Authorization: `Bearer ${token}`,
              "Content-Type": "application/json",
          },
      }).then(resp => {
          var rooms = resp.data
          var bookingRoom = this.$store.state.bookingRoom;
          var roomBooked = rooms.find((el) => el.id === bookingRoom.room);
          this.bookingRoom = roomBooked;
          console.log(this.bookingRoom);
          this.bookedDate = this.$store.state.bookingRoom.created_date;
      }).catch(err => console.log(err))
    }
  },
  beforeCreate() {
    this.$store.commit('setCurrentUser', localStorage.getItem('user'))
    this.$store.commit('setBookingRoom', JSON.parse(localStorage.getItem('bookingRoom')))
  },
  created() {
    if (this.error === false) this.message.push(this.$store.state.message)
  },
  mounted() {  
    this.getisBooked()
  },
};
</script>

<style>
.message {
  padding: 10px;
  font-weight: bold;
  font-size: 12px;
  color: white;
  background: #0d6efd;
  border-radius: 10px;
}

.print {
  font-style: italic;
  font-size: 12px;
  font-weight: bold;
}

.delete {
  font-style: italic;
  font-size: 12px;
  font-weight: bold;
  color: rgb(27, 26, 26);
}

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
