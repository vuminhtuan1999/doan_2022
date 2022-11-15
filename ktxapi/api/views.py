from turtle import update
from django import views
from django.shortcuts import render
from requests import delete, request
from rest_framework import viewsets, filters
from rest_framework.generics import GenericAPIView, ListAPIView

from api.models import Profile, BookingLaundryService, BookingRoom, BookingStudyRoom, Building, Notification, Payment, Profile, Room, Room_User, StudyRoom, User, Reflect, TypeLaundryService
from .serializers import BookingLaundryServiceSerializer, NotifitionSerializer, PaymentSerializer, ProfileSerializer, TypeLaundryServiceSerializer, CadresSerializer, BookingRoomSerializer, BookingStudyRoomSerializer, BuildingSerializer, LoginSerializer, ReflectSerializer, RoomSerializer, RoomUserSerializer, StudyRoomSerializer, UserSerializer
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from .jwt import JWTAuthentication
from api import serializers
from rest_framework.pagination import PageNumberPagination

# Create your views here.
# class TestViewSet():
#      response.Response({"test":"123"})

class DefaultPagination(PageNumberPagination) :
    page_size_query_param = 'size'

class AuthUserAPIView(GenericAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated,]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        print(self,213)
        # serializer = self.serializer_class(user)

        return response.Response({'user' : serializer.data})

class RegisterAPIView(GenericAPIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CadresRegisterView(GenericAPIView):
    serializer_class = CadresSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        email = request.data.get('email', None)
        # print(email)

        password = request.data.get('password', None)
        user = authenticate(username=email,password=password)
        if user:
            serializer = self.serializer_class(user)
            # print(serializer)
            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response({'message': "Wrong Account"}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer
    pagination_class = DefaultPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'username', 'email', 'student_code', 'course_year')
    
    queryset = User.objects.all()
    
class ProfileViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    def create(self, request, *args, **kwargs):
        profileData = request.data
        
        newData = Profile.objects.create(
            first_name=profileData["first_name"],
            last_name=profileData["last_name"],
            bod=profileData["bod"],
            gender=profileData["gender"],
            folk=profileData["folk"],
            dtut=profileData["dtut"],
            religion=profileData["religion"],
            type_study=profileData["type_study"],
            user=User.objects.get(id=profileData["user"]),
        )
        newData.save()
        serializer = self.serializer_class(newData)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BuildingViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated,]
    serializer_class = BuildingSerializer
    pagination_class = DefaultPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'building_name')
    queryset = Building.objects.all()
    
class RoomViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated,]
    pagination_class = DefaultPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'room_name')
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    
class RoomByBuildingView(ListAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'room_name')
    serializer_class = RoomSerializer

    def get_queryset(self):
        # id = request.query_params.get("id")
        id = self.kwargs['id']
        building = Building.objects.get(id=id)
        rooms = Room.objects.filter(building=building)
        return rooms
    
class RoomUserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = RoomUserSerializer
    queryset = Room_User.objects.all()
    
    def create(self, request, *args, **kwargs):
        roomUserData = request.data
        
        newData = Room_User.objects.create(user=User.objects.get(id=roomUserData["user"]), room=Room.objects.get(id=roomUserData["room"]))
        newData.save()
        serializer = self.serializer_class(newData)
        updateRoom = Room.objects.get(id=roomUserData["room"])
        updateRoom.booked_number += 1
        updateRoom.note += User.objects.get(id=roomUserData["user"]).course_year + ","
        updateRoom.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BookingRoomViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingRoomSerializer
    pagination_class = DefaultPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id')
    queryset = BookingRoom.objects.all()
    
    def create(self, request, *args, **kwargs):
        bookingRoomData = request.data
        
        newbookingRoom = BookingRoom.objects.create(user=User.objects.get(id=bookingRoomData["user"]), room=Room.objects.get(id=bookingRoomData["room"]))
        newbookingRoom.save()
        
        serializer = self.serializer_class(newbookingRoom)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BookingRoomGetListUserView(ListAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        # id = request.query_params.get("id")
        id = self.kwargs['id']
        room = Room.objects.get(id=id)
        roomsuser = Room_User.objects.filter(room=room)
        idUserList = Room_User.objects.filter(room=room).values_list('user', flat=True)
        print(idUserList[1])
        users = []
        for userId in idUserList:
            user = User.objects.get(id=userId)
            users.append(user)
        return users
    
class TypeLaundryViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TypeLaundryServiceSerializer
    queryset = TypeLaundryService.objects.all()
    
class BookingLaundryViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingLaundryServiceSerializer
    pagination_class = DefaultPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id')
    queryset = BookingLaundryService.objects.all()
    
    def create(self, request, *args, **kwargs):
        booking = request.data
        
        newBookService = BookingLaundryService.objects.create(user=User.objects.get(id=booking["user"]), type=TypeLaundryService.objects.get(id=booking["type"]))
        newBookService.save()
        
        serializer = self.serializer_class(newBookService)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
class StudyRoomViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = StudyRoomSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id', 'room_name']
    
    queryset = StudyRoom.objects.all()
    
class BookingStudyRoomViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingStudyRoomSerializer
    queryset = BookingStudyRoom.objects.all()
    
    def create(self, request, *args, **kwargs):
        bookingStudyRoomData = request.data
        
        student_code = bookingStudyRoomData["student_code"]
        seat = bookingStudyRoomData["seat"]
        booking_date = bookingStudyRoomData["booking_date"]
        newBooking = BookingStudyRoom.objects.create(student_code=student_code, seat=seat, booking_date=booking_date, study_room=StudyRoom.objects.get(id=bookingStudyRoomData["study_room"]))
        newBooking.save()
        serializer = self.serializer_class(newBooking)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BookingStudyByRoomListView(ListAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingStudyRoomSerializer
    
    def get_queryset(self):
        id = self.kwargs['id']
        study_room = StudyRoom.objects.get(id=id)
        bookingStudyRoom = BookingStudyRoom.objects.filter(study_room=study_room)
        return bookingStudyRoom
    
class ReflectViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReflectSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id', 'note']
    queryset = Reflect.objects.all().order_by('-danger')
    
    def create(self, request, *args, **kwargs):
        formData = request.data
        type_reflect = formData["type_reflect"]
        danger = formData["danger"]
        note = formData["note"]
        isSeenByAdmin = formData.get("isSeenByAdmin")
        newReflect = Reflect.objects.create(room=Room.objects.get(id=formData["room"]), type_reflect=type_reflect, danger=danger, note=note, isSeenByAdmin=isSeenByAdmin)
        newReflect.save()
        serializer = self.serializer_class(newReflect)
        
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

class ReflectByRoomIDView(ListAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id', 'note']
    serializer_class = ReflectSerializer
    
    def get_queryset(self):
        id = self.kwargs['id']
        room = Room.objects.get(id=id)
        reflects = Reflect.objects.filter(room=room)
        
        return reflects
    
class PaymentViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id', 'name']
    queryset = Payment.objects.all()
    
    def create(self, request, *args, **kwargs):
        payment = request.data
        
        newPayment = Payment.objects.create(room=Room.objects.get(id=payment["room"]), name=payment["name"], cost=payment["cost"])
        newPayment.save()
        
        serializer = self.serializer_class(newPayment)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    

class PaymentByRoomView(ListAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer
    
    def get_queryset(self):
        id = self.kwargs['id']
        room = Room.objects.get(id=id)
        payments = Payment.objects.filter(room=room)
        
        return payments
    
class NotificationViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotifitionSerializer
    queryset = Notification.objects.all()
    
    def create(self, request, *args, **kwargs):
        notification = request.data
        
        newNoti = Notification.objects.create(user=User.objects.get(id=notification["user"]), content=notification["content"])
        newNoti.save()
        
        serializer = self.serializer_class(newNoti)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
class NotificationByUserView(ListAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotifitionSerializer
    
    def get_queryset(self):
        id = self.kwargs['id']
        user = User.objects.get(id=id)
        notifications = Notification.objects.filter(user=user)
        
        return notifications