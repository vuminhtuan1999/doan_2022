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
                      <th>Đã đăng kí</th>
                      <th>Đối tượng phòng kí túc xá</th>
                      <th>Giá phòng trên tháng</th>
                      <th>Đăng kí</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="room in this.rooms"
                      :key="room.id"
                      class="text-center"
                    >
                      <td>{{ room.id }}</td>
                      <td>{{ room.room_name }}</td>
                      <td>
                        {{ room.booked_number }} / {{ room.max_number }} ({{
                          room.type_room
                        }})
                      </td>
                      <td>{{ room.note }}</td>
                      <td>{{ room.month_cost }}</td>
                      <td>
                        <span v-if="this.isBooked === 1" class="btn btn-danger"
                          >Bạn không thể đăng kí thêm</span
                        >
                        <p v-else-if="this.isBooked === 2" style="color: blue">
                          Bạn đã có phòng
                        </p>
                        <button
                          v-else
                          class="btn btn-primary btn-action"
                          @click="bookingRoom(room.id)"
                        >
                          <i class="material-icons">check</i>
                          Đăng kí
                        </button>
                      </td>
                    </tr>
                  </tbody>

                  <tfoot>
                    <tr>
                      <th>#</th>
                      <th>Tên Phòng</th>
                      <th>Đã đăng kí</th>
                      <th>Đối tượng phòng kí túc xá</th>
                      <th>Giá phòng trên tháng</th>
                      <th>Đăng kí</th>
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

<script src="">
import Header from "../Header.vue";
import NavBar from "../NavBar.vue";
import Footer from "../Footer.vue";
import $ from "jquery";
import axios from "axios";
export default {
  name: "ListRoom",
  components: {
    Header,
    NavBar,
    Footer,
  },
  data() {
    return {
      isBooked: 0,
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
    async getisBooked() {
      var token = this.$store.state.token
      var currentUserID = parseInt( this.$store.state.curentUser )
      axios.get('/api/booking-room/', {
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
            localStorage.setItem('isBooked', this.isBooked)

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
    bookingRoom(roomId) {
      var token = this.$store.state.token;
      var userId = this.$store.state.curentUser;
      const formData = {
        user: userId,
        room: roomId,
      };
      axios
        .post("/api/booking-room/", formData, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((resp) => {
          console.log("Dang ki thanh cong");
          this.$store.commit("setBookingRoom", resp.data);
          localStorage.setItem('bookingRoom', JSON.stringify(resp.data))
          this.isBooked = 1
          localStorage.setItem('isBooked', this.isBooked)
          this.$store.commit('setMessage', 'Your Request Successfully!!!')
          this.$router.push({name : 'BookingRoom'});
        })
        .catch((err) => console.log(err));
    },
    async getListRoom() {
      this.showNextBtn = false
      this.showPreviousBtn = false
      var token = this.$store.state.token;
      await axios
        .get(`/api/room/?page=${this.currentPage}&size=${this.page_size}&search=${this.query}`, {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        })
        .then((resp) => {
          // this.rooms = this.$store.state.rooms;
          if (this.page_size === 0) {
            this.number_page = 1
            this.rooms = resp.data
          } else {
            this.count_of_data = resp.data.count
            this.getNumberPage()
            this.rooms = resp.data.results;
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
  },
  mounted() {
    this.getisBooked();
    this.getListRoom();
  },
  beforeCreate() {
    this.$store.commit('setCurrentUser', localStorage.getItem('user'))
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
