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
                      <th style="width: 15px">#</th>
                      <th>Ảnh Đại Diện</th>
                      <th>Username</th>
                      <th>Email</th>
                      <th>Mã Số Sinh Viên</th>
                      <th>Chuyên Ngành</th>
                      <th style="width: 15px">Khóa</th>
                      <th>Loại</th>
                      <th>Số Điện Thoại</th>
                      <th>Địa Chỉ</th>
                      <th>Trạng thái</th>
                      <th>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="user in this.users"
                      :key="user.id"
                      class="text-center"
                    >
                      <td>
                        <p>{{ user.id }}</p>
                      </td>
                      <td>
                        <img
                          :src="user.image"
                          style="width: 70px; height: 55px"
                        />
                      </td>
                      <td>
                        <p>{{ user.username }}</p>
                      </td>
                      <td>
                        <p>{{ user.email }}</p>
                      </td>
                      <td>
                        <p>{{ user.student_code }}</p>
                      </td>
                      <td>
                        <p>{{ user.specialization }}</p>
                      </td>
                      <td>
                        <p>{{ user.course_year }}</p>
                      </td>
                      <td>
                        <p class="type admin" v-if="user.is_admin">Admin</p>
                        <p class="type cadres" v-else-if="user.is_cadres">
                          Cán Bộ
                        </p>
                        <p class="type student" v-else-if="user.is_student">
                          Sinh Viên
                        </p>
                      </td>
                      <td>
                        <p>{{ user.phone_number }}</p>
                      </td>
                      <td>
                        <p>{{ user.address }}</p>
                      </td>
                      <td>
                        <p class="active-student" v-if="user.is_active">
                          Đã kích hoạt
                        </p>
                        <p class="disable-student" v-else>Đã vô hiệu</p>
                      </td>
                      <td class="action">
                        <button v-if="user.is_active" class="btn btn-danger">
                          Disable
                        </button>
                        <button
                          v-else-if="!user.is_active"
                          class="btn btn-success"
                        >
                          Actice
                        </button>
                        <button
                          class="btn btn-primary"
                          @click="detailUser(user.id)"
                          data-bs-toggle="modal"
                          data-bs-target="#exampleModal"
                        >
                          Chi tiết
                        </button>
                      </td>
                    </tr>
                  </tbody>

                  <tfoot>
                    <tr>
                      <th>#</th>
                      <th>Ảnh Đại Diện</th>
                      <th>Username</th>
                      <th>Email</th>
                      <th>Mã Số Sinh Viên</th>
                      <th>Chuyên Ngành</th>
                      <th>Khóa</th>
                      <th>Loại</th>
                      <th>Số Điện Thoại</th>
                      <th>Địa Chỉ</th>
                      <th>Trạng thái</th>
                      <th>Actions</th>
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
            <img :src="this.user.image" style="width: 150px; height: 80px" />
            <hr />
            <h5>Username</h5>
            <p>{{ user.username }}</p>
            <hr />
            <h5>Email</h5>
            <p>{{ user.email }}</p>
            <hr />
            <h5>Mã số sinh viên</h5>
            <p>{{ user.student_code }}</p>
            <hr />
            <h5>Chuyên ngành</h5>
            <p>{{ user.specialization }}</p>
            <hr />
            <h5>Khóa</h5>
            <p>{{ user.course_year }}</p>
            <hr />
            <h5>Điện Thoại</h5>
            <p>{{ user.phone_number }}</p>
            <hr />
            <h5>Địa chỉ</h5>
            <p>{{ user.address }}</p>
          </div>
          <div class="modal-footer">
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
import $ from "jquery";
import axios from "axios";
export default {
  name: "Users",
  components: {
    Header,
    NavBar,
    Footer,
  },
  data() {
    return {
      users: [],
      user: {},
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
      this.getListUser()
    },
    goPrePage() {
      this.currentPage -= 1
      this.getListUser()
    },
    choosePage(i) {
      this.currentPage = i
      this.getListUser()
    },
    changePageSize(e) {
      this.page_size = parseInt(e.target.value)
      this.number_page = 0
      this.getListUser()
    },
    search(e) {
      this.query = e.target.value
      if (this.query !== '') {
        this.getListUser()
      }
      this.getListUser()
    },
    detailUser(userId) {
      this.user = this.users.find((el) => el.id === userId);
    },
    async getListUser() {
      this.showNextBtn = false
      this.showPreviousBtn = false
      var token = this.$store.state.token;
      await axios
        .get(`/api/user/?page=${this.currentPage}&size=${this.page_size}&search=${this.query}`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((resp) => {
          if (this.page_size === 0) {
            this.number_page = 1
            this.users = resp.data
          } else {
            this.count_of_data = resp.data.count
            this.getNumberPage()
            this.users = resp.data.results;
          }
          
          if (resp.data.next) {
            this.showNextBtn = true
          }

          if (resp.data.previous) {
            this.showPreviousBtn = true
          }
          console.log(this.users);
        })
        .catch((err) => console.log(err));
      
    }
  },
  mounted() {
    this.getListUser()
    
  },
  created() {
    
  },
};
</script>

<style scoped>
#admin-list-user_wrapperroom {
  margin-top: 20px;
  margin-bottom: 20px;
  box-shadow: 0 0 20px rgb(0 0 0 / 11%);
  background-color: #ffffff;
  padding: 30px;
  border-radius: 5px;
}
#admin-list-user {
  padding: 30px 0px;
}
.btn-action {
  width: 150px;
  border-radius: 50px;
  border: none;
  background: rgb(123, 97, 226);
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

.main-content {
  background-color: #f2f3f8;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
  font-size: 14px;
  max-width: 100%;
}

table {
  table-layout: fixed;
  width: 100%;
}
table tbody td {
  max-width: 150px; /* Customise it accordingly */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

p.type {
  margin-top: 8px;
  padding: 5px;
  border-radius: 10px;
}

.admin {
  color: rgba(255, 255, 255, 0.863);
  font-weight: bold;
  background: rgb(219, 26, 26);
}

.cadres {
  color: rgba(255, 255, 255, 0.863);
  font-weight: bold;
  background: rgb(242, 0, 255);
}

.student {
  color: rgba(255, 255, 255, 0.863);
  font-weight: bold;
  background: rgb(32, 32, 196);
}

button {
  margin-top: 5px;
}

.action {
  display: flex;
  flex-direction: column;
}

/* .image {
    width: 70px !important;
  } */
</style>
