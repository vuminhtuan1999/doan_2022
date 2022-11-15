<template>
<div class="body-register">
  <div class="container">
		<form @submit.prevent="registerSubmit" enctype="multipart/form-data">
		<input type="checkbox" name="" id="flip">
		<div class="cover">
			<div class="front">
				<img src="../../public/img/login.jpg" alt="">
			</div>
			<div class="back">
				<img class="backImg" src="../../public/img/login.jpg" alt="">
			</div>
		</div>
			<div class="form-content">
			<div class="signup-form">
				<div class="title">Đăng ký</div>
                <div v-if="this.error">
                    <div v-for="(m, index) in this.message" :key="index" class="alert alert-danger alert-dismissible fade show" role="alert" style="padding : 3px">
                        <strong>Error!</strong> {{m}}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                </div>

                <div v-if="this.success">
                    <div v-for="(m, index) in this.message" :key="index" class="alert alert-success alert-dismissible fade show" role="alert" style="padding : 3px">
                        <strong>Success!</strong> {{    m}}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                </div>

				<div class="input-boxes">
					<div class="input-box">
						<i class="material-icons">pin</i>
                        &nbsp;&nbsp;
						<input type="text" placeholder="Mã Số Sinh Viên" v-model="student_code" required>
					</div>
					<div class="input-box">
						<i class="material-icons">person</i>
                        &nbsp;&nbsp;
						<input type="text" placeholder="Username" v-model="username" required>
					</div>
					<div class="input-box">
						<i class="material-icons">image</i>
                        &nbsp;&nbsp;
						<input type="file" placeholder="Ảnh đại diện" ref="file" @change="selectFile" required>
					</div>
					<div class="input-box">
						<i class="material-icons">email</i>
                        &nbsp;&nbsp;
						<input type="text" placeholder="Email" v-model="email" required>
					</div>
					<div class="input-box">
						<i class="material-icons">contacts</i>
                        &nbsp;&nbsp;
						<input type="text" placeholder="Địa chỉ" v-model="address" required>
					</div>
                    <div class="input-box">
						<i class="material-icons">phone</i>
                        &nbsp;&nbsp;
						<input type="text" placeholder="Số Điện Thoại" v-model="phone_number" required>
					</div>
					<div class="input-box">
						<i class="material-icons">key</i>
                        &nbsp;&nbsp;
						<input type="password" placeholder="Nhập mật khẩu" v-model="password" required>
					</div>
					<div class="input-box">
						<i class="material-icons">key</i>
                        &nbsp;&nbsp;
						<input type="password" placeholder="Nhập lại mật khẩu" v-model="confirm_password" required>
					</div>
					<div class="input-box">
						<i class="material-icons">auto_stories</i>
                        &nbsp;&nbsp;
						<input type="text" placeholder="Chuyên ngành" v-model="specialization" required>
					</div>
					<div class="input-box">
						<i class="material-icons">school</i>
                        &nbsp;&nbsp;
						<input type="text" placeholder="Khóa học" v-model="course_year" required>
					</div>
					<div class="button input-box">
						<i class="fas fa-envelope"></i>
						<input type="submit" value="Đăng ký">
					</div>
					<div class="text sign-up-text">Bạn đã có tài khoản? <router-link :to="{name: 'Login'}">Đăng nhập tại đây</router-link></div>
				</div>
			</div>
		</div>
		</form>	
	</div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignUp',
  data() {
        return {
            username: '',
            password: '',
            confirm_password: '',
            email: '',
            student_code: '',
            address: '',
            phone_number: '',
            image: '',
            specialization: '',
            course_year: '',
            is_student: true,
            is_cadres: false,
            error: false,
            message: [],
            success: false
        }
    },
    methods: {
        selectFile() {
            console.log(this.$refs.file);
            this.image = this.$refs.file.files[0]
        },
        registerSubmit() {
            this.error = false
            this.success = false
            this.message = []
            if (this.confirm_password !== this.password) {
                this.message.push('Two password not match!!! Please input same password')
                this.error = true
                return
            }
            const formData = {
                username: this.username,
                password: this.password,
                email: this.email,
                student_code: this.student_code,
                address: this.address,
                phone_number: this.phone_number,
                image: this.image,
                specialization: this.specialization,
                course_year: this.course_year,
                is_student: this.is_student,
                is_cadres: this.is_cadres
            }
            axios.post('/api/register', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(resp => {
                this.message.push("Create account Successfully!!!")
                this.success = true
                this.error = false
            }).catch(err => {
                console.log(err);
                this.message = Object.values(err.response.data)
                this.error = true
            })
        }
    }
}
</script>

<style scoped>
    @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap");

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

.body-register{
    padding: 30px;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-image: linear-gradient(135deg, #8ac1ef, #ca6ce9, #8ac1ee, #e93356);
    animation:gradient 10s ease infinite;
    background-size: 400% 400%;
    color: #333333;
}
.material-icons {
  font-family: 'Material Icons';
  font-weight: normal;
  font-style: normal;
  font-size: 28px !important;  /* Preferred icon size */
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
  font-feature-settings: 'liga';
}

.container {
    position: relative;
    max-width: 850px;
    width: 100%;
    background: #fff;
    padding: 40px 30px;
    box-shadow: 0 5px 10px rgba(0,0,0,0.2);
    perspective: 2700px;
}


.container .cover{
    position: absolute;
    top: 0;
    left: 50%;
    height: 100%;
    width: 50%;
    z-index: 98;
    transition: all 1s ease;
    transform-origin: left;
    transform-style: preserve-3d;
}

.container .cover::before{
    content: "";
    position: absolute;
    height: 100%;
    width: 100%;
    /* background: #7d2ae8;
    opacity: 0.2; */
    z-index: 100 ;
}

.container .cover::after{
    content: "";
    position: absolute;
    height: 100%;
    width: 100%;
    /* background: #7d2ae8; */
    /* opacity: 0.5; */
    z-index: 100;
    transform: rotateY(180deg);
}

.container #flip:checked ~ .cover {
    transform: rotateY(-180deg);
}

.container .form{
    height: 100%;
    width: 100%;
    background: #fff;
}

.container .form-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.form-content .login-form,
.form-content .signup-form{
    width: calc(100% / 2 - 25px);
}
form .form-content .title {
    position: relative;
    font-size: 24px;
    font-weight: 500;
    color: #333;
}

form .form-content .title:before {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    height: 3px;
    width: 25px;
    background: #7d2ae8;
}

form .signup-form  .title:before{
    width: 20px;
}

form .form-content .input-boxes {
    margin-top: 30px;
}

form .form-content .input-box {
    display: flex;
    align-items: center;
    height: 50px;
    width: 100%;
    margin: 10px 0;
    position: relative;
}

.form-content .input-box input {
    height: 100%;
    width: 100%;
    outline: none;
    border: none;
    padding: 0 30px;
    font-size: 16px;
    font-weight: 500;
    border-bottom: 2px solid rgba(0,0,0,0.2);
    transition: all 0.3s ease;
}

.form-content .input-box input:focus
.form-content .input-box input:valid{
    border-color: #7d2ae8;
}

.form-content .input-box i {
    position: absolute;
    color: #7d2ae8;
    font-size: 17px;
}

form .form-content .button{
    color: #fff;
    margin-top: 40px;
}

form .form-content .text{
    font-size: 14px;
    font-weight: 500;
    color: #333;
}

form .form-content .text a{
    text-decoration: none;
}

form .form-content .text a:hover{
    text-decoration: underline;
}

form .form-content .button input {
    color: #fff;
    background: #7d2ae8;
    border-radius: 6px;
    padding: 0;
    cursor: pointer;
    transition: all 0.4 ease;
}

form .form-content .button input:hover {
    background: #5b13b9;

}

form .form-content a{
    color: #5b13b9;
    cursor: pointer;
}

form .form-content a:hover{
    text-decoration: underline;
}

.container .cover img{
    position: absolute;
    height: 100%;
    width: 100%;
    object-fit: cover;
    z-index: 12;
    backface-visibility: hidden;
}

.container .cover .back .backImg{
    transform: rotateY(-180deg);
}


.container .cover .text{
    position: absolute;
    z-index: 111;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.cover .text .text-1,
.cover .text .text-2 {
    font-size: 26px;
    font-weight: 600;
    color: #fff;
    text-align: center;
    backface-visibility: hidden;
}


.cover .back .text .text-1,
.cover .back .text .text-2 {
    transform: rotateY(180deg);
}

.cover .text .text-2 {
    font-size: 15px;
    font-weight: 500;
    color: #fff;
    text-align: center;
    backface-visibility: hidden;
}

form .form-content .login-text,
form .form-content .sign-up-text {
    text-align: center;
    margin-top: 25px;
}

@media (max-width: 730px) {
    .container .cover{
        display: none;
    }
    .form-content, .signup-form{
        width: 200%;
        text-align: center;
    }   
    .container #flip:checked ~ form .signup-form{
        display: block;
    }
    .container #flip:checked ~ form .login-form{
        display: none;
    }
}

.container #flip{
    display: none;
}
</style>