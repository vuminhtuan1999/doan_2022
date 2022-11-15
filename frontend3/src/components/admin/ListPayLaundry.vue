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
          Quản Lý Hóa Đơn Dịch Vụ Giặt Là
        </h3>
        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">Thêm phòng</button>
        
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
                      <th>Người đăng kí</th>
                      <th>Mã Số Sinh Viên</th>
                      <th>Gói Dịch Vụ</th>
                      <th>Thành Tiền (VNĐ)</th>
                      <th>Trạng Thái</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="booking in this.bookings" :key="booking.id">
                        <th>{{booking.id}}</th>
                        <th>{{this.getUserById(booking.user).username}}</th>
                        <th>{{this.getUserById(booking.user).student_code}}</th>
                        <th>{{this.getTypeLaundryById(booking.type).type_name}}</th>
                        <th>{{this.getTypeLaundryById(booking.type).cost}}</th>
                        <th v-if="booking.isPay" style="color: green">Đã Thanh Toán</th>
                        <th v-else-if="!booking.isPay" style="color: red">Chưa Thanh Toán</th>
                        <th>
                            <button class="btn btn-success">
                                <i class="material-icons">feedback</i>
                                Gửi thông báo nhắc nhở
                            </button>
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

    <!-- Modal Thêm Phòng -->
    <!-- <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Thêm phòng</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="addNewRoom" id="form-add-room">
                <div class="form-group">
                    <label for="name">Tên phòng</label>
                    <input type="text" v-model="this.room.room_name" class="form-control" placeholder="Tên phòng" required>
                </div>
                <div class="form-group">
                    <label for="formGroupExampleInput2">Số Ghế Ngồi</label>
                    <input type="number" class="form-control" v-model="this.room.number_seat" placeholder="Số Lượng Ghế Ngồi" required>
                </div>
                <div class="form-group">
                    <label for="formGroupExampleInput2">Địa Chỉ Phòng</label>
                    <input type="text" class="form-control" v-model="this.room.room_position" placeholder="Địa Chỉ Phòng" required>
                </div>
              </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Đóng</button>
                <button type="submit" form="form-add-room" class="btn btn-primary">Thêm</button>
            </div>
          </div>
      </div>
    </div> -->

    <!-- Modal Sửa Phòng -->
    <!-- <div class="modal fade" id="exampleModal1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Sửa phòng</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                  <label for="name">Tên phòng</label>
                  <input type="text" class="form-control" id="name" placeholder="Tên ph">
              </div>
              <div class="form-group">
                  <label for="formGroupExampleInput2">Another label</label>
                  <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="Another input">
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Đóng</button>
            <button type="button" class="btn btn-primary">Sửa</button>
          </div>
        </div>
      </div>
    </div> -->

    <!-- Modal Xóa Phòng -->
    <!-- <div class="modal fade" id="exampleModal2" tabindex="-1" ref="deleteModal" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Xóa phòng</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
              Bạn có chắc chắn muốn xóa không?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Không</button>
            <button type="button" class="btn btn-danger" @click="confirmDelete">Có</button>
          </div>
        </div>
      </div>
    </div> -->

  </div>
</template>

<script src="">
import Header from "../Header.vue";
import NavBar from "../NavBar.vue";
import Footer from "../Footer.vue";
import $ from "jquery";
import axios from "axios";
export default {
  name: "ListPayLaundry",
  components: {
    Header,
    NavBar,
    Footer,
  },
  data() {
    return {
      bookings: [],
      users: [],
      types: [],
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

    getUserById(userid) {
        let user = new Object(this.users.find(el => el.id === userid))
        return user
    },
    getTypeLaundryById(typeid) {
        let type = new Object(this.types.find(el => el.id === typeid))
        return type
    },

    async getListTypeLaundry() {
        let token = this.$store.state.token;
        await axios.get(`/api/type-laundry/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        }).then(resp => {
            this.types = resp.data
        }).catch(err => console.log(err))
    },
    async getListBooking() {
      this.showNextBtn = false
      this.showPreviousBtn = false
      let token = this.$store.state.token;
      await axios
        .get(`/api/booking-service/?page=${this.currentPage}&size=${this.page_size}&search=${this.query}`, {
          headers: {
            'Authorization': `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        })
        .then((resp) => {
          if (this.page_size === 0) {
            this.number_page = 1
            this.bookings = resp.data
          } else {
            this.count_of_data = resp.data.count
            this.getNumberPage()
            this.bookings = resp.data.results;
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
    async getListUser() {
        let token = this.$store.state.token;

        await axios.get(`/api/user/?size=0`, {
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
    this.getListTypeLaundry();
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