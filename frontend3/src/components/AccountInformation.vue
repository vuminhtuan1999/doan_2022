<template>
    <div class="wrapper to" id="wrapper">
        <!-- Slide bar -->
        <NavBar/>

        <!-- Page content -->
        <div id="content">
            <div class="top-navbar">
                <Header/>
            </div>

            <!-- Main content -->
            <div class="main-content">
                <!-- <h3 style="margin:20px 0px;">
                    <i class="material-icons">
                        arrow_circle_right
                    </i>
                    Quản lý hồ sơ
                </h3> -->
                <h3 style="margin:20px 0px;">
                    <i class="material-icons">
                        arrow_circle_right
                    </i>
                    Quản lý hồ sơ
                </h3>
                <div v-if="!this.error && this.message[0] !== '' && this.message[0] !== undefined" class="alert alert-success alert-dismissible fade show" role="alert" style="padding : 3px">
                    <strong>Success!</strong> {{this.message[0]}}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>

                <div v-if="this.error">
                    <div v-for="(m, index) in this.message" :key="index" class="alert alert-danger alert-dismissible fade show" role="alert" style="padding : 3px">
                        <strong>Error!</strong> {{m}}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                </div>
                <form id="update-profile" @submit.prevent="updateProfile">
                <table class="table">
                    
                    <tbody>
                        <tr>
                            <td class="row" style="padding: 0; color: #5d78ff; height: 45px">
                                <div class="" style="border-bottom: 2px solid #5d78ff; width: 150px;display: flex;
    align-items: center;"><i class="fa fa-user mr-2" aria-hidden="true"></i>Quản lý hồ sơ</div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Username</div>
                                <div class="col-12 col-md-8">{{this.user.username}}</div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">E-mail</div>
                                <div class="col-12 col-md-8">{{this.user.email}}</div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Mã Số Sinh Viên</div>
                                <div class="col-12 col-md-8">{{this.user.student_code}}</div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Số điện thoại</div>
                                <div class="col-12 col-md-8">{{this.user.phone_number}}</div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Chuyên Ngành</div>
                                <div class="col-12 col-md-8">{{this.user.specialization}}</div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Khóa</div>
                                <div class="col-12 col-md-8">{{this.user.course_year}}</div>
                            </td>
                        </tr>

                        <tr v-if="this.currentProfile">
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Họ và Tên</div>
                                <div class="col-12 col-md-8">{{this.currentProfile.first_name}} {{this.currentProfile.last_name}}</div>
                            </td>
                        </tr>

                        <tr v-if="this.currentProfile">
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Ngày Sinh</div>
                                <div class="col-12 col-md-8">{{this.currentProfile.bod}}</div>
                            </td>
                        </tr>

                        <tr v-if="this.currentProfile">
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Giới Tính</div>
                                <div class="col-12 col-md-8">{{this.currentProfile.gender}}</div>
                            </td>
                        </tr>

                        <tr v-if="this.currentProfile">
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Dân Tộc</div>
                                <div class="col-12 col-md-8">{{this.currentProfile.folk}}</div>
                            </td>
                        </tr>

                        <tr v-if="this.currentProfile">
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Đối Tượng Ưu Tiên</div>
                                <div class="col-12 col-md-8">{{this.currentProfile.dtut}}</div>
                            </td>
                        </tr>

                        <tr v-if="this.currentProfile">
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Tôn Giáo</div>
                                <div class="col-12 col-md-8">{{this.currentProfile.religion}}</div>
                            </td>
                        </tr>

                        <tr v-if="this.currentProfile">
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Loại hình Đào Tạo</div>
                                <div class="col-12 col-md-8">{{this.currentProfile.type_study}}</div>
                            </td>
                        </tr>
                        
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-5 row align-items-center">
                                    <div class="col-5 text-right"><label >Họ</label></div>
                                    <div class="col-7">
                                        <input v-model="this.profile.first_name" type="text" placeholder="Họ" class="form-control" required/>
                                    </div>
                                    
                                </div>
                                <div class="col-12 col-md-5 row align-items-center">
                                    <div class="col-5 text-right"><label >Đệm và Tên</label></div>
                                    <div class="col-7" style="padding-bottom: 7px; font-size: 12px">
                                        <input v-model="this.profile.last_name" type="text" placeholder="Tên Đệm và Tên" class="form-control" required/>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-5 row align-items-center">
                                    <div class="col-5 text-right"><label >Ngày Sinh</label></div>
                                    <div class="col-7">
                                        <input v-model="this.profile.bod" type="date" class="form-control" required/>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-5 row align-items-center">
                                <div class="col-5 text-right"><label >Giới tính</label></div>
                                <div class="col-7">
                                        <select v-model="this.profile.gender" class="form-select" aria-label="Default select example" required>
                                            <option value="Nam" selected>Nam</option>
                                            <option value="Nữ">Nữ</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-12 col-md-5 row align-items-center">
                                    <div class="col-5 text-right"><label >Dân tộc</label></div>
                                     <div class="col-7">
                                        <select v-model="this.profile.folk" class="form-select" aria-label="Default select example" required>
                                            <option value="">Chọn</option>
                                            <option value="Kinh" selected>Kinh</option>
                                            <option value="Tày">Tày</option>
                                            <option value="Thái">Thái</option>
                                            <option value="Hoa">Hoa</option>
                                            <option value="Khơ-me">Khơ-me</option>
                                            <option value="Mường">Mường</option>
                                            <option value="Nùng">Nùng</option>
                                            <option value="Hmông ">Hmông</option>
                                            <option value="Dao">Dao</option>
                                            <option value="Gia-rai">Gia-rai</option>
                                            <option value="Ngái">Ngái</option>
                                            <option value="Ê-đê">Ê-đê</option>
                                            <option value="Ba-na">Ba-na</option>
                                            <option value="Xơ-đăng">Xơ-đăng</option>
                                            <option value="Sán Chay">Sán Chay</option>
                                            <option value="Cơ-ho">Cơ-ho</option>
                                            <option value="Chăm">Chăm</option>
                                            <option value="Sán Dìu">Sán Dìu</option>
                                            <option value="Hrê">Hrê</option>
                                            <option value="Mnông">Mnông</option>
                                            <option value="Ra-glai">Ra-glai</option>
                                            <option value="Xtiêng">Xtiêng</option>
                                            <option value="Bru-Vân Kiều">Bru-Vân Kiều</option>
                                            <option value="Thổ">Thổ</option>
                                            <option value="Giáy">Giáy</option>
                                            <option value="Cơ-tu">Cơ-tu</option>
                                            <option value="Gié-Triêng">Gié-Triêng</option>
                                            <option value="Mạ">Mạ</option>
                                            <option value="Khơ-mú">Khơ-mú</option>
                                            <option value="Co">Co</option>
                                            <option value="Ta-ôi">Ta-ôi</option>
                                            <option value="Chơ-ro">Chơ-ro</option>
                                            <option value="Kháng">Kháng</option>
                                            <option value="Xinh-mun">Xinh-mun</option>
                                            <option value="Hà Nhì">Hà Nhì</option>
                                            <option value="Chu-ru">Chu-ru</option>
                                            <option value="Lào">Lào</option>
                                            <option value="La Chi">La Chi</option>
                                            <option value="La Ha">La Ha</option>
                                            <option value="Phù Lá">Phù Lá</option>
                                            <option value="La Hủ">La Hủ</option>
                                            <option value="Lự">Lự</option>
                                            <option value="Lô Lô">Lô Lô</option>
                                            <option value="Chứt">Chứt</option>
                                            <option value="Mảng">Mảng</option>
                                            <option value="Pà Thẻn">Pà Thẻn</option>
                                            <option value="Cơ Lao">Cơ Lao</option>
                                            <option value="Cống">Cống</option>
                                            <option value="Bố Y">Bố Y</option>
                                            <option value="Si La">Si La</option>
                                            <option value="Pu Péo">Pu Péo</option>
                                            <option value="Brâu">Brâu</option>
                                            <option value="Ơ Đu">Ơ Đu</option>
                                            <option value="Rơ-măm">Rơ-măm</option>
                                            <option value="Người nước ngoài">Người nước ngoài</option>
                                        </select>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-5 row align-items-center">
                                    <div class="col-5 text-right"><label >Đối tượng ưu tiên</label></div>
                                    <div class="col-7">
                                        <select v-model="this.profile.dtut" class="form-select" aria-label="Default select example" required>
                                            <option value="">Chọn</option>
                                            <option value="0" selected>0-Không có</option>
                                            <option value="1">1-AH; TB; BB</option>
                                            <option value="2">2-CCBCM</option>
                                            <option value="3">3-CAH</option>
                                            <option value="4">4-CAH</option>
                                            <option value="5">5-CLS</option>
                                            <option value="6">6-CTB</option>
                                            <option value="7">7-CBB</option>
                                            <option value="8">8-CNTB</option>
                                            <option value="9">9-CĐHH</option>
                                            <option value="10">10-MC</option>
                                            <option value="11">11-DT-ĐBKK</option>
                                            <option value="12">12-TT</option>
                                            <option value="13">13-CT</option>
                                            <option value="14">14-HN-DT</option>
                                            <option value="15">15-XĐBKK-DT</option>
                                            <option value="16">16-TNLĐ</option>
                                        </select>
                                    </div>
                                    
                                </div>
                                <div class="col-12 col-md-5 row align-items-center">
                                    <div class="col-5 text-right"><label >Tôn giáo</label></div>
                                    <div class="col-7">
                                        <select v-model="this.profile.religion" class="form-select" aria-label="Default select example" required>
                                            <option value="">Chọn</option>
                                            <option value="Không" selected>Không</option>
                                            <option value="Phật giáo">Phật giáo</option>
                                            <option value="Công giáo">Công giáo</option>
                                            <option value="Cao Đài">Cao Đài</option>
                                            <option value="Hòa Hảo">Hòa Hảo</option>
                                            <option value="Tin Lành">Tin Lành</option>
                                            <option value="Hồi Giáo">Hồi Giáo</option>
                                            <option value="Bà La Môn">Bà La Môn</option>
                                            <option value="Khác">Khác</option>
                                        </select>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-5 row align-items-center">
                                    <div class="col-5 text-right"><label >Loại hình đào tạo</label></div>
                                    <div class="col-7">
                                        <select v-model="this.profile.type_study" class="form-select" aria-label="Default select example" required>
                                            <option value="">Chọn</option>
                                            <option value="Đại học" selected>Đại học</option>
                                            <option value="Cao đẳng nghề">Cao đẳng nghề</option>
                                            <option value="Cao học, NCS">Cao học, NCS</option>
                                            <option value="Khác">Khác</option>
                                        </select>
                                    </div>
                                    
                                </div>
                                
                            </td>
                        </tr>
                        
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right">Ảnh thẻ sinh viên</div>
                                <div class="col-12 col-md-4">
                                    Chú ý: Sinh viên upload ảnh thẻ sinh viên rõ nét, có thể chụp bằng điện thoại.
                                    <img :src="`${this.baseURL}${this.user.image}`" class="rounded mx-auto d-block" style="width: 150px; height: 200px">
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right"></div>
                                <div class="col-12 col-md-4">
                                    <button type="submit" class="btn btn-primary" form="update-profile">Cập nhật hồ sơ</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table class="table">
                    
                    <tbody>
                        <tr>
                            <td class="row" style="padding: 0; color: #5d78ff; height: 45px">
                                <div class="" style="border-bottom: 2px solid #5d78ff; width: 150px;display: flex;
    align-items: center;"><i class="fa fa-user mr-2" aria-hidden="true"></i>Thay đổi mật khẩu</div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-7 row align-items-center">
                                    <div class="col-5 text-right"><label >Mật khẩu hiện tại</label></div>
                                    <div class="col-7">
                                        <input type="password" class="form-control "/>
                                    </div>
                                    
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-7 row align-items-center">
                                    <div class="col-5 text-right"><label >Mật khẩu mới</label></div>
                                    <div class="col-7">
                                        <input type="password" class="form-control "/>
                                    </div>
                                    
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-7 row align-items-center">
                                    <div class="col-5 text-right"><label >Xác nhận mật khẩu mới</label></div>
                                    <div class="col-7">
                                        <input type="password" class="form-control "/>
                                    </div>
                                    
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="row">
                                <div class="col-12 col-md-4 text-md-right"></div>
                                <div class="col-12 col-md-8">
                                    <button class="btn btn-primary">Cập nhật hồ sơ</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                </form>
                <!-- Footer -->
                <!-- <div class="footer-style">
                    <Footer/>
                </div> -->
            </div>
        </div>
    </div>
  
</template>

<script src="">
import Header from '../components/Header.vue'
import NavBar from '../components/NavBar.vue'
// import Footer from '../components/Footer.vue'
import $ from 'jquery'
import axios from 'axios'
export default {
    name: 'AccountInformation',
    components: {
        Header,
        NavBar,
        // Footer
    },
    data() {
        return {
            error: false,
            message: [],
            user : {},
            baseURL : '',
            profile: {
                id: 0,
                first_name: '',
                last_name: '',
                bod: '',
                gender: '',
                folk: '',
                dtut: '',
                religion: '',
                type_study: '',
            },
            currentProfile: {}
        }
    },
    methods: {
        updateProfile() {
            this.error = false
            this.message = []
            Date.prototype.yyyymmdd = function() {
                var yyyy = this.getFullYear();
                var mm = this.getMonth() < 9 ? "0" + (this.getMonth() + 1) : (this.getMonth() + 1); // getMonth() is zero-based
                var dd = this.getDate() < 10 ? "0" + this.getDate() : this.getDate();
                return "".concat(yyyy).concat('-').concat(mm).concat('-').concat(dd);
            };
            let date = new Date(this.profile.bod)
            date = date.yyyymmdd()
            let token = this.$store.state.token
            let formData = {
                first_name: this.profile.first_name,
                last_name: this.profile.last_name,
                bod: date,
                gender: this.profile.gender,
                folk: this.profile.folk,
                dtut: this.profile.dtut,
                religion: this.profile.religion,
                type_study: this.profile.type_study,
                user: this.user.id
            }
            console.log(this.profile.id);
            if (this.profile.id) {
                axios.put(`/api/user-profile/${this.profile.id}/`, formData, {
                    headers: {
                        'Authorization': `Bearer ${token}`,
                        "Content-Type": "application/json",
                    },
                }).then(resp => {
                    this.message.push('Update successfully!!')
                    this.error = false
                    this.getProfile()
                }).catch(err => {
                    this.message = Object.values(err.response.data)
                    this.error = true
                })
            }else {
                axios.post('/api/user-profile/', formData, {
                    headers: {
                        'Authorization': `Bearer ${token}`,
                        "Content-Type": "application/json",
                    },
                }).then(resp => {
                    this.message.push('Update successfully!!')
                    this.error = false
                    this.getProfile()
                    
                }).catch(err => {
                    this.message = Object.values(err.response.data)
                    this.error = true
                })
            }

           
        },
        async getProfile() {
            let token = this.$store.state.token
            await axios.get('/api/user-profile/', {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            }).then(resp => {
                let temp = resp.data.filter(el => el.user === this.user.id)
                if (temp) {
                    this.profile.id = temp[0].id
                    this.currentProfile = temp[0]
                } 
                else this.profile.id = 0
            }).catch(err => console.log(err))
        },
        async getCurrentUser() {
            let token = this.$store.state.token
            await axios.get('/api/auth', {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    "Content-Type": "application/json",
                },
            }).then(resp => {
                this.user = resp.data.user
                console.log(this.user);
            })
            .catch(err => console.log(err))
        }
    },
    mounted() {
        this.baseURL = axios.defaults.baseURL
        this.getCurrentUser()
        this.getProfile()
    }

}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Po');
    h3 {
        font-size: 22px;
    }
    .main-content{
        background-color: #f2f4f8 !important;
        font-family: "Helvetica Neue", Helvetica, "Noto Sans", sans-serif, Arial, sans-serif
    }
    .row{
        /* border-radius: 5px; */
        background: white;
        font-size: 12px;
        font-weight: 400;
        color: #646c9a;
    }
    input::-webkit-outer-spin-button,
    input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
    }
    select {
        font-size: 12px;
    }
</style>