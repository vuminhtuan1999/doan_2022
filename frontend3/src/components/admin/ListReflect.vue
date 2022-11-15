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
          Quản lý hỗ trợ, phản ánh
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
                      <th>Ngày Phản Ánh</th>
                      <th>Loại</th>
                      <th>Trạng Thái</th>
                      <th>Mô tả</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="reflect in this.reflects" :key="reflect.id">
                      <th>{{ reflect.id }}</th>
                      <th>{{ this.getRoomName(reflect.room) }}</th>
                      <th>{{ reflect.created_date }}</th>
                      <th>{{ getTypeReflectString(reflect.type_reflect) }}</th>
                      <th v-if="reflect.danger" class="level danger">Cần Gấp (cháy nổ, an ninh trật tự)</th>
                      <th v-else class="level non-danger">Không cần gấp</th>
                      <th>{{ reflect.note }}</th>
                      <th>
                        <button class="btn btn-success" v-if="!reflect.isSeenByAdmin" @click="processReflect(reflect)">Xử lý</button>
                        <button class="btn btn-primary" v-else-if="reflect.isSeenByAdmin">
                            <i class="material-icons">hourglass_empty</i>
                            Đang Xử lý
                        </button>
                        &nbsp;&nbsp;
                        <button class="btn btn-danger" data-toggle="modal" data-target="#exampleModal" @click="deleteReflect(reflect.id)">
                            <i class="material-icons" style="font-weight: bold; font-size: 14px !important">clear</i>
                        </button>
                      </th>
                      <!-- <th v-if="reflect.isSeenByAdmin" class="isSeen">Đã tiếp nhận được phản ánh</th>
                      <th v-else class="non-isSeen">Chưa được xử lý</th> -->
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

    <!-- Modal Xóa Phòng -->
    <div class="modal fade" id="exampleModal" tabindex="-1" ref="deleteModal" aria-labelledby="exampleModalLabel" aria-hidden="true">
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
      reflects: [],
      rooms: [],
      reflectId: 0,
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
      this.getListReflect()
    },
    goPrePage() {
      this.currentPage -= 1
      this.getListReflect()
    },
    choosePage(i) {
      this.currentPage = i
      this.getListReflect()
    },
    changePageSize(e) {
      this.page_size = parseInt(e.target.value)
      this.number_page = 0
      this.getListReflect()
    },
    search(e) {
      this.query = e.target.value
      if (this.query !== '') {
        this.getListReflect()
      }
      this.getListReflect()
    },

    processReflect(reflect) {
        let token = this.$store.state.token
        
        let formData = {
            room: reflect.room,
            type_reflect: reflect.type_reflect,
            danger: reflect.danger ? "True" : "False",
            note: reflect.note,
            isSeenByAdmin: "True"
        }

        axios.put(`/api/reflect/${reflect.id}/`, formData, {
            headers: {
                'Authorization': `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        }).then(resp => {
            console.log("Success");
            this.getListReflect()
        }).catch(err => console.log(err))
        
    },

    deleteReflect(id) {
        this.reflectId = id
        console.log('duong xư lu')
    },

    confirmDelete() {
        let token = this.$store.state.token

        axios.delete(`/api/reflect/${this.reflectId}/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        }).then(resp => {
            console.log("Success");
            this.currentPage = 1
            this.getListReflect()
            window.$('#exampleModal').modal('hide')
        }).catch(err => console.log(err))
    },
    getRoomName(roomid) {
        let room = new Object(this.rooms.find(el => el.id === roomid))
        return room.room_name
    },
    getTypeReflectString(type_reflect) {
      if (type_reflect === 1) return "Điện nước và hư hỏng khác"
      else if (type_reflect === 2) return "An ninh trật tự, Vệ sinh môi trường"
      else if (type_reflect === 3) return "Hỗ trợ phần mềm trực tuyến"
      else return ""
    }, 

    async getListReflect() {
      this.showNextBtn = false
      this.showPreviousBtn = false
      var token = this.$store.state.token;
      await axios
        .get(`/api/reflect/?page=${this.currentPage}&size=${this.page_size}&search=${this.query}`, {
          headers: {
            'Authorization': `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        })
        .then((resp) => {
          // this.rooms = this.$store.state.rooms;
          if (this.page_size === 0) {
            this.number_page = 1
            this.reflects = resp.data
            console.log(this.reflects);
          } else {
            this.count_of_data = resp.data.count
            this.getNumberPage()
            this.reflects = resp.data.results;
            console.log(this.reflects);
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
  },
  mounted() {
    this.getListReflect();
    this.getListRoom();
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