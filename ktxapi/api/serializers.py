from ast import mod
from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import BookingLaundryService, BookingRoom, BookingStudyRoom, Notification, Payment, Profile, Reflect, Room_User, StudyRoom, TypeLaundryService, User, Building, Room


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "password", 
            # "email", 
            # "student_code", 
            # "address", 
            # "phone_number",
            # "image",
            # "specialization",
            # "course_year",
            # "is_active",
            "is_admin",
            "is_student",
            "is_cadres"
            ]
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}
        
        read_only_fields = ['is_admin', 'is_active']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class CadresSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "password", 
            "email", 
            "address", 
            "phone_number",
            "image",
            "is_active",
            "is_admin",
            "is_student",
            "is_cadres"
            ]
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}
        
        read_only_fields = ['is_admin']
    
class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'token', "is_admin","id","is_student"]
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}
        
        read_only_fields = ['token']

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'
        
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "room_name", "type_room", "booked_number", "max_number", "month_cost", "building", "note"]
        
        read_only_fields = ['booked_number', 'note']
        
        
class RoomUserSerializer(ModelSerializer):
    class Meta:
        model = Room_User
        fields = '__all__'
   
class BookingRoomSerializer(ModelSerializer):
    class Meta:
        model = BookingRoom
        fields = '__all__'     
        
class TypeLaundryServiceSerializer(ModelSerializer):
    class Meta:
        model = TypeLaundryService
        fields = '__all__'
        
class BookingLaundryServiceSerializer(ModelSerializer):
    class Meta:
        model = BookingLaundryService    
        fields = '__all__'    
        
class StudyRoomSerializer(ModelSerializer):
    class Meta:
        model = StudyRoom
        fields = '__all__'
        
class BookingStudyRoomSerializer(ModelSerializer):
    class Meta:
        model = BookingStudyRoom
        fields = '__all__'
        
class ReflectSerializer(ModelSerializer):
    class Meta:
        model = Reflect
        fields = '__all__'
        

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        
class NotifitionSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        
