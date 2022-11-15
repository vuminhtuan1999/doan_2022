<template>
    <nav class="navbar navbar-expand-md navbar-light bg-light fixed-top">
        <div class="container-fluid">
            <a class="navbar-brand" href="#"><img class="img-brand" src="../../public/img/logo.png"></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link trangchu" href="#">TRANG CHỦ</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link gioithieu" href="#">GIỚI THIỆU</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link thongbao" href="#">THÔNG BÁO</a>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link dangnhap" :to="{name: 'Login'}">ĐĂNG NHẬP</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link dangki" :to="{name: 'SignUp'}">ĐĂNG KÍ</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div id="slides" class="carousel slide" data-ride="carousel">
        <ul class="carousel-indicators">
            <li data-target="#slides" data-slide-to="0" class="active"></li>
            <li data-target="#slides" data-slide-to="1" class="active"></li>
            <li data-target="#slides" data-slide-to="2" class="active"></li>
        </ul>
        <div class="carousel-inner" style="height: 590px">
            <div class="carousel-item active" style="height: 100%">
                <img class="img-fluid" src="../../public/img/background.jpg" style="width: 100%;">
                <div class="carousel-caption d-flex"  style="height: 100%!important; align-items: center;">
                    <div style="width: 100% " class="">
                        <div class="col-md-4 col-12" style="margin: 0 auto;" >
                            <h1 class="display-2">KÝ TÚC XÁ ĐẠI HỌC THỦY LỢI</h1>
                        </div>
                        <h3 style="font-size: 1.75rem; margin-top: 25px; font-family: 'Oswald',serif;">Không gian vui chơi, học tập tuyệt vời</h3>
                    </div>
                </div>
            </div>
            <div class="carousel-item"  style="height: 100%">
                <img src="../../public/img/background1.jpg" style="width: 100%; height: 100%; object-fit: fill;">
                <div class="carousel-caption d-flex"  style="height: 100%!important; align-items: center;">
                    <div style="width: 100%" class="">
                        <div class="col-md-4 col-12" style="margin: 0 auto;">
                            <h1 class="display-2">KÝ TÚC XÁ ĐHBKHN</h1>
                        </div>
                        <h3 style="font-size: 1.75rem; margin-top: 25px; font-family: 'Oswald',serif;">Thể thao không giới hạn</h3>
                    </div>
                </div>
            </div>
            <div class="carousel-item"  style="height: 100%">
                <img src="../../public/img/background2.jpg" style="width: 100%; height: 100%; object-fit: fill;">
                <div class="carousel-caption d-flex"  style="height: 100%!important; align-items: center;">
                    <div style="width: 100%" class="">
                        <div class="col-md-4 col-12" style="margin: 0 auto;" >
                            <h1 class="display-2">KÝ TÚC XÁ ĐHBKHN</h1>
                        </div>
                        <h3 style="font-size: 1.75rem; margin-top: 25px; font-family: 'Oswald',serif;">Nơi tình yêu bắt đầu</h3>
                    </div>
                </div>
            </div>
        </div>
        <a class="carousel-control-prev" href="#slides" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true" style="width: 40px; height: 40px;"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#slides" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true" style="width: 40px; height: 40px;"></span>
            <span class="sr-only">Next</span>
          </a>
    </div>
    <div class="container-fluid tb">
        <div class="row welcome text-center">
            <div class="col-12">
                <h2 class="display-4" style="font-family: Tahoma, Verdana, Segoe, sans-serif; letter-spacing: 1px; text-transform: uppercase; font-size: 36px; padding: 30px;">THÔNG BÁO</h2>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-md-4" style="padding:   0px 10px;">
                <div class="card text-center" style="margin: 0px">
                    <img src="../../public/img/thongbao.jpg" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title"><a href="#">THÔNG BÁO CỦA TRUNG TÂM QL KTX</a></h5>
                        <p class="card-text">Hiện nay Trung tâm QL KTX đang xếp ở cho sinh viên vào các nhà trong khu nội trú KTX theo lịch học của nhà trường. Vậy Trung tâm QL KTX trân trọng thông báo để sinh viên được biết.</p>
                        <a href="#">Xem thêm</a>
                    </div>
                </div>
            </div>            
            <div class="col-md-4" style="padding: 0px 10px;">
                <div class="card text-center" style="margin: 0px">
                    <img src="../../public/img/thongbao.jpg" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title"><a href="#">THÔNG BÁO CỦA TRUNG TÂM QL KTX</a></h5>
                        <p class="card-text">Hiện nay Trung tâm QL KTX đang xếp ở cho sinh viên vào các nhà trong khu nội trú KTX theo lịch học của nhà trường. Vậy Trung tâm QL KTX trân trọng thông báo để sinh viên được biết.</p>
                        <a href="#">Xem thêm</a>
                    </div>
                </div>
            </div>
            
            <div class="col-md-4" style="padding: 0 10px;">
                <div class="card text-center" style="margin: 0px">
                    <img src="../../public/img/thongbao.jpg" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title"><a href="#">THÔNG BÁO CỦA TRUNG TÂM QL KTX</a></h5>
                        <p class="card-text">Hiện nay Trung tâm QL KTX đang xếp ở cho sinh viên vào các nhà trong khu nội trú KTX theo lịch học của nhà trường. Vậy Trung tâm QL KTX trân trọng thông báo để sinh viên được biết.</p>
                        <a href="#">Xem thêm</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container padding gt">
        <div class="row padding">
            <div class="col-lg-6" style="padding: 0 10px;">
                <h2 style="padding: 15px 0px">TT QUẢN LÝ KTX</h2>
                <p>Tổ chức, quản lý toàn diện khu KTX sinh viên. Bố trí xếp ở sinh viên nội trú đúng đối tượng, số lượng, đảm bảo thu lệ phí lưu trú của sinh viên nộp về trường đúng qui định; Đảm bảo đủ các điều kiện phục vụ sinh hoạt và học tập của sinh viên nội trú:
                    Điện, nước sinh hoạt, dịch vụ ăn uống.
                    An ninh trật tự, vệ sinh môi trường
                    Hoạt động thể thao và văn hoá tinh thần trong khu KTX.</p>
                    <br>
            </div>
            <div class="col-lg-6">
                <img src="../../public/img/quanlyktx.jpeg" class="img-fluid">
            </div>
        </div>    
    </div>
    <div class="container padding">
        <div class="row text-center padding">
            <div class="col-12" style="padding: 0px 10px 30px 10px">
                <h2>ĐƠN VỊ HỖ TRỢ</h2>
            </div>
            <div class="col-md-3 col-6" style="padding: 0 10px;">
                <img src="../../public/img/donvihotro.png" class="img-fluid" alt="">
            </div>
            <div class="col-md-3 col-6" style="padding: 0 10px;">
                <img src="../../public/img/donvihotro.png" class="img-fluid" alt="">
            </div>
            <div class="col-md-3 d-none d-md-block" style="padding: 0 10px;">
                <img src="../../public/img/donvihotro.png" class="img-fluid" alt="">
            </div>
            <div class="col-md-3 d-none d-md-block" style="padding: 0 10px;">
                <img src="../../public/img/donvihotro.png" class="img-fluid" alt="">
            </div>
        </div>
    </div>
    <footer>
        <div class="container-fluid padding">
        <div class="row text-center">
            <div class="col-md-4">
                <hr class="light">
                <h5>VP TRUNG TÂM</h5>
                <hr class="light">
                <p>Văn phòng: A4-101, 104</p>
                <p>Điện thoại: 11111111</p>
                <p>Email: ktx@wru.edu.vn</p>
            </div>
            <div class="col-md-4">
                <hr class="light">
                <h5>GIỜ LÀM VIỆC</h5>
                <hr class="light">
                <p>Thứ 2 đến thứ 6: 8 giờ sáng - 5 giờ chiều</p>
                <p>Thứ 7: 10 giờ sáng - 4 giờ chiều</p>
                <p>Chủ nhật: Đóng cửa</p>
            </div>
            <div class="col-md-4">
                <hr class="light">
                <h5>CHUYÊN MỤC</h5>
                <hr class="light">
                <p>New</p>
                <p>Uncategorized</p>
            </div>
            <div class="col-12">
                <hr class="light">
                <h5>&copy; tuanvm720@wru.com</h5>
            </div>
        </div>
        </div>
    </footer>
</template>

<script>
import $ from 'jquery'
export default {
    name: 'Home',
    components: {

    },
    mounted() {
        $(".thongbao").click(function() {
            $('html,body').animate({
                scrollTop: $(".tb").offset().top-65},
                'slow'); 
        });
        $(".gioithieu").click(function() {
            $('html,body').animate({
                scrollTop: $(".gt").offset().top-65},
                'slow'); 
        });
    }
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,700');


html, body{
    height: 100%;
    width: 100%;
    font-family: "Poppins" sans-serif;
}

/* .navbar {
    padding: .8rem;
} */

.navbar-nav li{
    padding-right: 20px;
}

.nav-link {
    font-size: 1.1rem !important;
}

.carousel-inner img{
    width: 100%;
    height: 100%;
}
.carousel-caption{
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
}

.jumbotron {
    padding: 1rem;
    border-radius: 0;
}


.padding{
    padding-top: 1rem;
    padding-bottom: 2rem;
}
footer {
    background-color: #3f3f3f;
    color: #d5d5d5;
    padding-top: 2rem;
}
hr.light {
    border-top: 1px solid #d5d5d5;
    width: 75%;
    margin-top: .8rem;
    margin-bottom: 1rem;
}

footer a {
    color: #d5d5d5;
}

hr.light-100 {
    border-top: 1px solid #d5d5d5;
    width: 100%;
    margin-top:  .8rem;
    margin-bottom: 1rem;
}

@media (max-width: 992px){
    .social a{
        font-size: 4em;
        padding: 2rem;
    }
}

.display-4{
    font-size: 300%;
}

@media(max-width: 768px){

}

@media(max-width:576px){

}



.carousel-item {
    transition: -webkit-transform 0.5s ease;
    transition: transform 0.5s ease;
    transition: transform 0.5s ease, -webkit-transform 0.5s ease;
    -webkit-backface-visibility: visible;
    backface-visibility: visible;
}

figure{
    position: relative;
    width: 100%;
    height: 60%;
    margin: 0!important;
}
.fixed-wrap {
    clip: rect(0, auto, auto, 0);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
#fixed {
    background-image: url("../../public/img/login.jpg");
    position: fixed;
    display: block;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center center;
    -webkit-transform: translateZ(0);
    transform: translateZ(0);
    will-change: transform;
}

[class*="col-"] {
    padding: 1rem;
}

.img-brand{
    width: 200px;
}

.display-2 {
    font-size: 2.5rem;
    font-weight: 400;
    line-height: 1.3;
    background: #009dea;
    font-family: 'Oswald',serif;
}

.card-body{
    box-shadow: 0 0 20px 7px rgba(0,0,0,0.1);
}
.card{
    margin: 20px 10px;
}
.card-body a{
    color: #0c7f90;
    text-decoration: none;
    font-size: 15px;
    margin-top: auto;
    font-weight: 600;
}
.card-body a:hover{
    color: #63a6b0 !important;
    text-decoration: none;
}

.card{
    margin: 0px;
}

[class*="col-"]{
    padding: 0px;
}
</style>