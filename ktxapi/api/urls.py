from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('building', views.BuildingViewSet)
router.register('room', views.RoomViewSet)
router.register('room-user', views.RoomUserViewSet)
router.register('booking-room', views.BookingRoomViewSet)
router.register('user', views.UserViewSet)
router.register('study-room', views.StudyRoomViewSet)
router.register('study-service', views.BookingStudyRoomViewSet, basename="StudyService")
router.register('reflect', views.ReflectViewSet)
router.register('type-laundry', views.TypeLaundryViewSet)
router.register('booking-service', views.BookingLaundryViewSet)
router.register('payment', views.PaymentViewSet)
router.register('notification', views.NotificationViewSet)
router.register('user-profile', views.ProfileViewSet)
# router.register('test',views.TestViewSet,basename='MyModel')

urlpatterns = [
     path('register', views.RegisterAPIView.as_view(), name="register"),
     path('cadres-register', views.CadresRegisterView.as_view(), name="cadres_register"),
     path('login', views.LoginAPIView.as_view(), name="login"),
     path('auth', views.AuthUserAPIView.as_view(), name="auth"),
     path('room-by-building/<int:id>/', views.RoomByBuildingView.as_view(), name="roombybuilding"),
     path('room-user-list/<int:id>/', views.BookingRoomGetListUserView.as_view(), name="getListUserOfRoom"),
     path('study-list/<int:id>/', views.BookingStudyByRoomListView.as_view(), name="getBookingByRoom"),
     path('reflectbyroom/<int:id>/', views.ReflectByRoomIDView.as_view(), name="reflectbyroom"),
     path('paymentbyroom/<int:id>/', views.PaymentByRoomView.as_view(), name="paymentbyroom"),
     path('notificationbyuser/<int:id>/', views.NotificationByUserView.as_view(), name="notificationbyuser"),
     path('', include(router.urls))
 ]
