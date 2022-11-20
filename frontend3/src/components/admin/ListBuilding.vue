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
          Quản lý tòa nhà
        </h3>
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addBuildingModal">Thêm tòa</button>
        

        <div class="container" id="user-list-building_wrapperroom">
            <div class="row dataTables_wrapper dt-bootstrap5 no-footer" id="user-list-building_wrapper">
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
            <!-- Sau khi thêm tòa nhà sẽ hiện đoạn này -->
                <div class="card mx-auto" style="width: 18rem;" v-for="bl in this.buildings" :key="bl.id">
                    <img class="card-img-top" :src="bl.image" style="width: 100%; height: 200px;">
                    <div class="card-body">
                        <h5 class="card-title">{{ bl.building_name }}</h5>
                        <p class="card-text">{{ bl.note }}</p>
                            <router-link :to="{name: 'ListRoom', params:{ id: bl.id }}" class="btn btn-sm btn-primary">Xem chi tiết các phòng</router-link>

                            <button class="btn btn-sm btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal1" @click="updateBuilding(bl.id)">Sửa</button>
                            
                            <!-- Modal sửa tòa nhà-->
                            <div class="modal fade" id="exampleModal1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Sửa tòa nhà</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <form id="form-update-building" @submit.prevent="confirmUpdate" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="building_name">Tên tòa nhà</label>
                                            <input v-model="this.building.building_name" type="text" class="form-control" id="building_name" placeholder="Tên tòa nhà" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="address">Địa chỉ</label>
                                            <input v-model="this.building.address" type="text" class="form-control" id="address" placeholder="Địa chỉ" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="note">Mô tả</label>
                                            <input v-model="this.building.note" type="text" class="form-control" id="note" placeholder="Mô tả" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="image">Ảnh tòa nhà</label>
                                            <input type="file" ref="updateFile" @change="updateFile"  class="form-control" id="image" placeholder="Ảnh tòa nhà" required>
                                        </div>
                                    </form>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Đóng</button>
                                    <button type="submit" class="btn btn-primary" form="form-update-building">Sửa</button>
                                </div>
                                </div>
                            </div>
                            </div>
                            <button class="btn btn-sm btn-danger" data-bs-toggle="modal" data-bs-target="#exampleModal2" @click="deleteBuilding(bl.id)">Xóa tòa nhà</button>
                            <!-- Modal -->
                            
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
        </div>


        <!-- Footer -->
        <div class="footer-style">
          <Footer />
        </div>
      </div>

      <!-- Modal Thêm Tòa Nhà -->
      <div class="modal fade" id="addBuildingModal" ref="addBuildingModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Thêm tòa nhà</h5>
                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
              <form id="form-add-building" @submit.prevent="addBuilding($event)" enctype="multipart/form-data">
                <div class="form-group">
                  <label for="building_name">Tên tòa nhà</label>
                  <input v-model="building.building_name" type="text" class="form-control" id="building_name" placeholder="Tên tòa nhà" required>
                </div>
                <div class="form-group">
                  <label for="address">Địa chỉ</label>
                  <input v-model="building.address" type="text" class="form-control" id="address" placeholder="Địa chỉ" required>
                </div>
                <div class="form-group">
                  <label for="note">Mô tả</label>
                  <input v-model="building.note" type="text" class="form-control" id="note" placeholder="Mô tả" required>
                </div>
                <div class="form-group">
                  <label for="image">Ảnh tòa nhà</label>
                  <input type="file" ref="file" @change="selectFile" class="form-control" id="image" placeholder="Ảnh tòa nhà" required>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Đóng</button>
              <button type="submit" form="form-add-building" class="btn btn-primary">Thêm</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal Sửa Tòa Nhà -->

      <!-- Modal Xóa Tòa Nhà -->
      <div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Xóa tòa nhà</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                Bạn có chắc chắn muốn xóa tòa nhà này không?
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Đóng</button>
                <button type="button" class="btn btn-danger" @click="confirmDelete">Xóa</button>
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
  name: "ListRoom",
  components: {
    Header,
    NavBar,
    Footer,
  },
  data() {
    return {
      buildings: [],
      buildingID: 0,
      building: {
        building_name: '',
        address: '',
        note: '',
        image: '',
      },
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
      this.getListBuilding()
    },
    goPrePage() {
      this.currentPage -= 1
      this.getListBuilding()
    },
    choosePage(i) {
      this.currentPage = i
      this.getListBuilding()
    },
    changePageSize(e) {
      this.page_size = parseInt(e.target.value)
      this.number_page = 0
      this.getListBuilding()
    },
    search(e) {
      this.query = e.target.value
      if (this.query !== '') {
        this.getListBuilding()
      }
      this.getListBuilding()
    },
    selectFile() {
        this.building.image = ''
        console.log(this.$refs.file.files[0]);
        this.building.image = this.$refs.file.files[0]
    },

    updateFile() {
        this.building.image = ''
        console.log(this.$refs.updateFile[0].files[0]);
        this.building.image = this.$refs.updateFile[0].files[0]
    },

    addBuilding(e) {
      
      let formData = {
        building_name: this.building.building_name,
        address: this.building.address,
        note: this.building.note,
        image: this.building.image
      }

      console.log(formData);
      let token = this.$store.state.token
      axios.post(`/api/building/`, formData, {
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'multipart/form-data',
          },
      }).then(resp => {
        console.log("Success");
        this.currentPage = 1
        this.getListBuilding()
      }).catch(err => console.log(err))
      
    },

    updateBuilding(id) {
      this.buildingID = id
      let temp = this.buildings.find(el => el.id === id)
      if (temp !== undefined) {
        this.building.building_name = temp.building_name
        this.building.address = temp.address
        this.building.note = temp.note
      }
    },
    confirmUpdate() {
      let formData = {
        building_name: this.building.building_name,
        address: this.building.address,
        note: this.building.note,
        image: this.building.image
      }

      console.log(formData);
      let token = this.$store.state.token
      axios.put(`/api/building/${this.buildingID}/`, formData, {
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'multipart/form-data',
          },
      }).then(resp => {
        console.log("Success");
        console.log(this.$refs.file);
        this.currentPage = 1
        this.getListBuilding()
        this.building.building_name = ''
        this.building.address = ''
        this.building.note = ''
      }).catch(err => console.log(err))
    },
    deleteBuilding(id) {
      this.buildingID = id
    },
    confirmDelete() {
      let token = this.$store.state.token
      axios.delete(`/api/building/${this.buildingID}/`, {
        headers: {
            'Authorization': `Bearer ${token}`,
            "Content-Type": "application/json",
          },
      }).then(resp => {
        console.log("Success")
        this.currentPage = 1
        this.getListBuilding()
        window.$('#exampleModal2').fade();
        
      }).catch(err => console.log(err))
    },
    async getListBuilding() {
      this.showNextBtn = false
      this.showPreviousBtn = false
      var token = this.$store.state.token;
      await axios
        .get(`/api/building/?page=${this.currentPage}&size=${this.page_size}&search=${this.query}`, {
          headers: {
            'Authorization': `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        })
        .then((resp) => {
          // this.rooms = this.$store.state.rooms;
          if (this.page_size === 0) {
            this.number_page = 1
            this.buldings = resp.data
          } else {
            this.count_of_data = resp.data.count
            this.getNumberPage()
            this.buildings = resp.data.results;
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
    this.getListBuilding();
    
  },
  beforeCreate() {
  }
};
</script>

<style scoped>

#user-list-building_wrapperroom {
  margin-top: 20px;
  margin-bottom: 20px;
  box-shadow: 0 0 20px rgb(0 0 0 / 11%);
  background-color: #ffffff;
  padding: 30px;
  border-radius: 5px;
}
#user-list-building {
  padding: 30px 0px;
}
.main-content {
  background-color: #f2f3f8;
  font-family: "Helvetica Neue", Helvetica, "Noto Sans", sans-serif, Arial,
    sans-serif;
  font-weight: 550;
}
h3 {
  font-size: 22px;
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
.card{
    background-color: rgb(246, 244, 244);
    padding-top: 10px;
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