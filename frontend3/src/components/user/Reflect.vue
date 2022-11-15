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
          Hỗ Trợ Phản Ánh
        </h3>
        <br>

        <button 
            class="btn btn-primary" 
            style="border-radius: 20px; font-size: 12px; width: 100px"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
        >
            Đăng Kí
        </button>
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
                      <th>Phòng</th>
                      <th>Ngày</th>
                      <th>Loại</th>
                      <th>Trạng Thái</th>
                      <th>Mô Tả</th>
                      <th>Kết Quả</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="reflect in this.reflects" :key="reflect.id">
                      <th>{{ reflect.id }}</th>
                      <th>{{ this.room.room_name }}</th>
                      <th>{{ reflect.created_date }}</th>
                      <th>{{ getTypeReflectString(reflect.type_reflect) }}</th>
                      <th v-if="reflect.danger" class="level danger">Cần Gấp (cháy nổ, an ninh trật tự)</th>
                      <th v-else class="level non-danger">Không cần gấp</th>
                      <th>{{ reflect.note }}</th>
                      <th v-if="reflect.isSeenByAdmin" class="isSeen">Đã tiếp nhận được phản ánh</th>
                      <th v-else class="non-isSeen">Chưa được xử lý</th>
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
          <div class="modal-body" style="height:500px; overflow:auto;">
            <div class="row">
                <div class="col-md-12">
                    <div class="panel panel-primary" data-collapsed="0">
                        <div class="panel-heading">
                            <div class="panel-title">
                                Đăng Kí
                            </div>
                            
                        </div>

                        <div class="panel-body">
                                <form
                                    id="add-reflect-form"
                                    class="form-horizontal form-groups-bordered validate"
                                    enctype="multipart/form-data"
                                >
                                    <div class="form-group">
                                        <label for="" class="col-sm-3 control-label">Loại Phản Ánh</label>
                                        <div class="col-sm-5">
                                            <select v-model="type_reflect" class="form-select form-select-sm required">
                                                <option value="1">Điện nước và hư hỏng khác</option>
                                                <option value="2">An ninh trật tự, Vệ sinh môi trường</option>
                                                <option value="3">Hỗ trợ phần mềm trực tuyến</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label for="" class="col-sm-3 control-label">Mô Tả</label>
                                        <div class="col-sm-9">
                                            <textarea v-model="note" class="form-control wysihtml5 required" required></textarea>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label for="" class="col-sm-3 control-label">Mức Độ</label>
                                        <div class="col-sm-5">
                                            <select v-model="danger" class="form-select form-select-sm required">
                                                <option value>Chọn</option>
                                                <option value="false">Không cần gấp</option>
                                                <option value="true">Cần gấp (cháy nổ, an ninh trật tự)</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-sm-3 control-label col-sm-offset-2"></div>
                                    
                                </form>
                        </div>
                    </div>
                </div>
            </div>
          </div>
          <div class="modal-footer">
            <button @click="addReflect" class="btn btn-primary" form="add-reflect-form">Gửi phản ánh</button>
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

<script src="">
import Header from "../Header.vue";
import NavBar from "../NavBar.vue";
import Footer from "../Footer.vue";
import $ from "jquery";
import axios from "axios";
export default {
  name: "Reflect",
  components: {
    Header,
    NavBar,
    Footer,
  },
  data() {
    return {
      reflects: [],
      room: {},
      type_reflect: 1,
      danger: false,
      note: '',
      isSeenByAdmin: false,
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
      this.getReflect()
    },
    goPrePage() {
      this.currentPage -= 1
      this.getReflect()
    },
    choosePage(i) {
      this.currentPage = i
      this.getReflect()
    },
    changePageSize(e) {
      this.page_size = parseInt(e.target.value)
      this.number_page = 0
      this.getReflect()
    },
    search(e) {
      this.query = e.target.value
      if (this.query !== '') {
        this.getReflect()
      }
      this.getReflect()
    },

    getTypeReflectString(type_reflect) {
      if (type_reflect === 1) return "Điện nước và hư hỏng khác"
      else if (type_reflect === 2) return "An ninh trật tự, Vệ sinh môi trường"
      else if (type_reflect === 3) return "Hỗ trợ phần mềm trực tuyến"
      else return ""
    }, 
    addReflect() {
      let token = this.$store.state.token;
      let danger = (this.danger) ? "True" : "False"
      let isSeenByAdmin = (this.isSeenByAdmin) ? "True" : "False"
      let formData = {
        room: this.room.id,
        type_reflect: this.type_reflect,
        danger: danger,
        note: this.note,
        isSeenByAdmin: isSeenByAdmin
      }
      console.log(JSON.stringify(formData));
      axios.post('/api/reflect/', JSON.stringify(formData), {
        headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
      }).then(resp => {
        console.log("Success")
        window.$('#exampleModal').modal('hide')
      })
      .catch(err => console.log(err))
    },
    async getReflect() {
      this.showNextBtn = false
      this.showPreviousBtn = false
      let token = this.$store.state.token;
      await axios
        .get(`/api/room-user/`, {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }).then(resp => {
          let roomID = 0
          let room_user = resp.data.find(el => el.user === parseInt(this.$store.state.curentUser))
          if (room_user) {
            roomID = room_user.room
          }
          if (roomID) {
            axios.get(`/api/reflectbyroom/${roomID}/?page=${this.currentPage}&size=${this.page_size}&search=${this.query}`, {
              headers: {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json",
              },
            }).then(resp => {
              
              if (this.page_size === 0) {
                this.number_page = 1
                this.reflects = resp.data
              } else {
                this.count_of_data = resp.data.count
                this.getNumberPage()
                this.reflects = resp.data.results
              }
              
              if (resp.data.next) {
                this.showNextBtn = true
              }

              if (resp.data.previous) {
                this.showPreviousBtn = true
              }

              this.room = this.getRoom(roomID)
            }).catch(err => console.log(err))
          }
        }).catch(err => console.log(err))
    },
    async getRoom(id) {
      let token = this.$store.state.token 
      await axios.get(`/api/room/${id}/`, {
        headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
      }).then(resp => {
        this.room = resp.data
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
    // this.isBooked = parseInt(this.$store.state.isBooked)
    this.getReflect();
  },
  beforeCreate() {
    this.$store.commit("setIsBooked", localStorage.getItem('isBooked'))
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

.panel-primary {
    border: 0;
    box-shadow: 0 0 20px rgb(0 0 0 / 11%);
}

.panel {
    margin-bottom: 17px;
    background-color: #fff;
    /* border: 1px solid transparent;
    border-radius: 3px;
    -webkit-box-shadow: 0 1px 1px rgb(0 0 0 / 5%);
    box-shadow: 0 1px 1px rgb(0 0 0 / 5%); */
}

.panel-primary .panel-heading {
    padding: 10px 15px;
    color: #fff;
    border: 0;
    background-color: #282a3c;
    border-radius: 4px 4px 0px 0px;
}

.panel-title {
    margin-top: 0;
    margin-bottom: 0;
    font-size: 14px;
    color: inherit;
}

.panel-body {
    padding: 15px;
}

.level {
  margin: 5px;
  font-size: 14px;
  font-weight: bold;
  color: white;
}

.danger {
  background-color: red;
}

.non-danger {
  background-color: orange;
}

.isSeen {
  color: green;
}

.non-isSeen {
  color: red
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
