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

        <div>
          <p style="color: blue">Mã số thành viên: 20172923</p>
          <p style="color: blue">Hạng thành viên : Mới</p>

          <br />

          <p style="color: red; text-align: center">
            Cho những sinh viên chưa biết:
          </p>

          <p>1. Thời gian mở phòng tự học : Tối các ngày trong tuần T2 - CN</p>
          <p>2. Giờ mở cửa : 18h30 - 22h30</p>
          <p>3. Có thể đăng kí trên trang web KTX Thủy Lợi</p>
          <p>4. Chỉ dành cho sinh viên tự học</p>
        </div>

        <br />

        <h6 style="font-weight: bold">Danh sách phòng tự học</h6>

        <div id="user-list-room_wrapperroom">
          <div
            class="dataTables_wrapper dt-bootstrap5 no-footer"
            id="table_export_wrapper"
          >
            <div class="row">
              <div class="col-sm-6">
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

              <div class="col-sm-6">
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
                  class="table table-bordered table-striped datatable dataTable no-footer"
                  style="width: 100%"
                >
                  <thead>
                    <tr role="row">
                      <th>#</th>
                      <th>Tên Phòng</th>
                      <th>Tổng chỗ ngồi</th>
                      <th>Chi tiết</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr class="odd" v-for="sr in this.study_rooms" :key="sr.id">
                      <th>{{ sr.id }}</th>
                      <th>{{ sr.room_name }}</th>
                      <th>{{ sr.number_seat }}</th>
                      <th>{{ sr.room_position }}</th>
                      <th>
                        <button
                          class="btn btn-danger btn-action"
                          @click="detailsRoom(sr.id)"
                          data-bs-toggle="modal"
                          data-bs-target="#exampleModal"
                        >
                          <i class="material-icons">assignment</i>
                          <span>Chi tiết</span>
                        </button>
                      </th>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div class="row">
              <div class="col-sm-5">
                <div id="user-list-room_info" class="dataTables_info">
                  Showing 0 to 0 of 0 entries
                </div>
              </div>

              <div class="col-sm-7">
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

    <!-- Modal -->
    <div
      class="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">
              Thông Tin Người Dùng
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div v-if="this.messageDate !== ''" class="alert alert-danger alert-dismissible fade show" role="alert" style="padding : 3px">
                    <strong>Error!</strong> {{this.messageDate}}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
            <h5 style="font-size: 16px">Đặt phòng theo lịch</h5>
            <input type="date" name="" id="booking-date">
            <hr>
            <div class="chair-list">
                
                <div class="chair" v-for="(n, index) in this.room.number_seat" :key="index">
                    <p style="color: #00a65a; font-weight: bold">{{index + 1}}</p>
                    <button 
                        class="btn btn-success" 
                        :class="{
                            booked: checkBooked(index + 1), 
                            disabled: checkBooked(index + 1),
                            choose: this.seat_choose === (index + 1)
                            }" 
                        @click="chooseChair(index + 1)"
                    >
                        <i class="material-icons" style="font-size: 44px !important;">chair</i>
                    </button>
                    <p v-if="checkBooked(index + 1)" style="font-size: 10px; color: red; font-weight: bold">{{getStudentCode(index + 1)}}</p>
                    
                    
                </div>
                
            </div>
          </div>
          <div class="modal-footer">
            <button v-if="!checkExistStudentCode()" class="btn btn-primary" :class="{disabled: !this.ischoose}" @click="getSeat">Đặt chỗ</button>
            <button v-else class="btn btn-danger" @click="deleteSeat">Hủy Đặt Chỗ</button>
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "../Header.vue";
import NavBar from "../NavBar.vue";
import Footer from "../Footer.vue";
import axios from "axios";
import $ from 'jquery'
export default {
  name: "StudyRoom",
  components: {
    Header,
    NavBar,
    Footer,
  },
  data() {
    return {
      messageDate: '',
      ischoose: false,
      seat_choose: 0,
      bookeds: [],
      room: {},
      study_rooms: [],
      page_size: 1,
      number_page: 0,
      count_of_data: 0,
      showNextBtn: false,
      showPreviousBtn: false,
      currentPage: 1,
      query: "",
    };
  },
  methods: {
    getNumberPage() {
      this.number_page =
        this.count_of_data % this.page_size === 0
          ? this.count_of_data / this.page_size
          : parseInt(this.count_of_data / this.page_size) + 1;
    },
    goNextPage() {
      this.currentPage += 1;
      this.getListStudyRoom();
    },
    goPrePage() {
      this.currentPage -= 1;
      this.getListStudyRoom();
    },
    choosePage(i) {
      this.currentPage = i;
      this.getListStudyRoom();
    },
    changePageSize(e) {
      this.page_size = parseInt(e.target.value);
      this.number_page = 0;
      this.getListStudyRoom();
    },
    search(e) {
      this.query = e.target.value;
      if (this.query !== "") {
        this.getListStudyRoom();
      }
      this.getListStudyRoom();
    },
    async getListStudyRoom() {
      this.showNextBtn = false;
      this.showPreviousBtn = false;
      var token = this.$store.state.token;
      await axios
        .get(
          `/api/study-room/?page=${this.currentPage}&size=${this.page_size}&search=${this.query}`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
              "Content-Type": "application/json",
            },
          }
        )
        .then((resp) => {
          // this.rooms = this.$store.state.rooms;
          if (this.page_size === 0) {
            this.number_page = 1;
            this.study_rooms = resp.data;
          } else {
            this.count_of_data = resp.data.count;
            this.getNumberPage();
            this.study_rooms = resp.data.results;
          }

          if (resp.data.next) {
            this.showNextBtn = true;
          }

          if (resp.data.previous) {
            this.showPreviousBtn = true;
          }
        })
        .catch((err) => console.log(err));
    },
    detailsRoom(id) {
      this.room = this.study_rooms.find(el => el.id === id)
      let token = this.$store.state.token;
      axios
        .get(`/api/study-list/${id}/`, {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        })
        .then((resp) => {
          this.bookeds = resp.data;
        });
    },
    checkBooked(i) {
        let temp = this.bookeds.find(el => el.seat === i)
        if (temp !== undefined) return true
        return false
    },
    getStudentCode(i) {
        let temp = this.bookeds.find(el => el.seat === i)
        return temp.student_code
    },
    chooseChair(i) {
        if (!this.ischoose) {
            this.ischoose = true
            this.seat_choose = i
        } else {
            this.ischoose = false
            this.seat_choose = 0
        }
        
    },
    getSeat() {
        Date.prototype.yyyymmdd = function() {
          var yyyy = this.getFullYear();
          var mm = this.getMonth() < 9 ? "0" + (this.getMonth() + 1) : (this.getMonth() + 1); // getMonth() is zero-based
          var dd = this.getDate() < 10 ? "0" + this.getDate() : this.getDate();
          return "".concat(yyyy).concat('-').concat(mm).concat('-').concat(dd);
        };
        let dateInput = document.getElementById('booking-date');
        if (!dateInput.value) {
          this.messageDate = 'Xin vui lòng chọn ngày';
          return;
        }


        let booking_date = new Date(dateInput.value)
        let booking_date_string = booking_date.yyyymmdd()

        let token = this.$store.state.token
        console.log(this.$store.state.student_code,);
        let formData = {
            student_code: this.$store.state.student_code,
            seat: this.seat_choose,
            study_room: this.room.id,
            booking_date: booking_date_string
        }
        axios.post('/api/study-service/', formData, {
            headers: {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        }).then(resp => {
          console.log("Đặt chỗ thành công")
          window.alert('đặt oke')
          window.$('#exampleModal').modal('hide')
          this.seat_choose = 0

        }).catch(err => console.log(err))
    },
    checkExistStudentCode() {
      let temp = this.bookeds.find(el => el.student_code === this.$store.state.student_code)
      console.log('check student code', this.bookeds)
      if (temp) {
        
        return true}
      return false
    },
    deleteSeat() {
      let token = this.$store.state.token
      let temp = this.bookeds.find(el => el.student_code === this.$store.state.student_code)
      if (temp) {
        axios.delete(`/api/study-service/${temp.id}/`, {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          }
        }).then(resp => {
          console.log("Hủy đặt chỗ thành công");
          window.alert(' huyr đặt oke')

          window.$('#exampleModal').modal('hide')
          this.seat_choose = 0
        }).catch(err => console.log(err))
      }
    }
  },
  
  mounted() {
    this.getListStudyRoom();
    
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth()+1; //January is 0 so need to add 1 to make it 1!
    let yyyy = today.getFullYear();
    if(dd<10){
      dd='0'+dd
    } 
    if(mm<10){
      mm='0'+mm
    } 

    today = yyyy+'-'+mm+'-'+dd;
    document.getElementById("booking-date").setAttribute("min", today);
  },
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

.btn-action {
  font-size: 12px;
}

.booked {
    background-color: red;
}

.choose {
    background-color: yellow;
}

.chair-list {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}

.chair {
    margin-bottom: 20px;
    margin-right: 40px;
}

input[type="date"] {
  background-color: #129d55;
  padding: 15px;
  color: #ffffff;
  font-size: 14px;
  border: none;
  outline: none;
  border-radius: 5px;
}

::-webkit-calendar-picker-indicator {
  background-color: #ffffff;
  padding: 5px;
  cursor: pointer;
  border-radius: 3px;
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
