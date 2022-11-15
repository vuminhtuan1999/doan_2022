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
        <h3 style="margin: 20px 0px 10px 0px">
          <i class="material-icons"> arrow_circle_right </i>
          Quản lý đặt phòng
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
                    <input type="search" v-model="query" @change="search($event)" class="form-control form-control-sm" />
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
                      <th>#</th>
                      <th>Tên Phòng</th>
                      <th>Mã Số Sinh Viên</th>
                      <th>Email Sinh Viên</th>
                      <th>Ngày Đăng Kí</th>
                      <th>Duyệt</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="b in this.bookings" :key="b.id">
                        <th>{{b.id}}</th>
                        <th>{{this.getRoomName(b.room)}}</th>
                        <th>{{this.getUser(b.user).student_code}}</th>
                        <th>{{this.getUser(b.user).email}}</th>
                        <th>{{b.created_date}}</th>
                        <th>
                            <button class="btn btn-warning" @click="confirmBooking(b.id, b.room, b.user)">Duyệt</button>
                        </th>
                    </tr>
                  </tbody>
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

<script src="">
import Header from "../Header.vue";
import NavBar from "../NavBar.vue";
import Footer from "../Footer.vue";
import $ from "jquery";
import axios from "axios";
export default {
  name: "ListBookingRoom",
  components: {
    Header,
    NavBar,
    Footer,
  },
  data() {
    return {
      bookings: [],
      users: [],
      rooms: [],
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
      this.getListBooking()
    },
    goPrePage() {
      this.currentPage -= 1
      this.getListBooking()
    },
    choosePage(i) {
      this.currentPage = i
      this.getListBooking()
    },
    changePageSize(e) {
      this.page_size = parseInt(e.target.value)
      this.number_page = 0
      this.getListBooking()
    },
    search(e) {
      this.query = e.target.value
      if (this.query !== '') {
        this.getListBooking()
      }
      this.getListBooking()
    },

    confirmBooking(bookingID, roomID, userID) {
        let token = this.$store.state.token

        axios.delete(`/api/booking-room/${bookingID}/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        }).then(resp => {
            let formData = {
                room: roomID,
                user: userID
            }
            axios.post(`/api/room-user/`, formData,{
                headers: {
                    'Authorization': `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            }).then(resp => console.log("Success"))
            .catch(err => console.log(err))
        }).catch(err => console.log(err))
    },
    getRoomName(roomid) {
        let room = new Object(this.rooms.find(el => el.id === roomid))
        return room.room_name
    },

    getUser(userid) {
        let user = new Object(this.users.find(el => el.id === userid))
        return user
    },
    async getListBooking() {
      this.showNextBtn = false
      this.showPreviousBtn = false
      var token = this.$store.state.token;
      await axios
        .get(`/api/booking-room/?page=${this.currentPage}&size=${this.page_size}&search=${this.query}`, {
          headers: {
            'Authorization': `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        })
        .then((resp) => {
          // this.rooms = this.$store.state.rooms;
          if (this.page_size === 0) {
            this.number_page = 1
            this.bookings = resp.data
            console.log(this.bookings);
          } else {
            this.count_of_data = resp.data.count
            this.getNumberPage()
            this.bookings = resp.data.results;
            console.log(this.bookings);
          }
          
          if (resp.data.next) {
            this.showNextBtn = true
          }

          if (resp.data.previous) {
            this.showPreviousBtn = true
          }
        })
        .catch((err) => console.log(err));
    },
    async getListRoom() {
        let token = this.$store.state.token
        await axios.get('/api/room/?size=0', {
            headers: {
            'Authorization': `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }).then(resp => {
            this.rooms = resp.data
        }).catch(err => console.log(err))
    },
    async getListUser() {
        let token = this.$store.state.token
        await axios.get('/api/user/?size=0', {
            headers: {
            'Authorization': `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }).then(resp => {
            this.users = resp.data
        }).catch(err => console.log(err))
    }
  },
  mounted() {
    this.getListBooking();
    this.getListRoom();
    this.getListUser();
  },
  beforeCreate() {
  }
};
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

.btn{
    font-size: 12px;
}
.btn-info {
  background-color: #42a5f5 !important;
  color: #ffffff;
  border-radius: 5px;
  font-size: 16px !important;
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