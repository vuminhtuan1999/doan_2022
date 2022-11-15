from django.db import models

# Create your models here.
from lib2to3.pgen2 import token
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from django.utils import timezone
from django.contrib.auth.hashers import make_password
import jwt
from django.conf import settings
from datetime import datetime, timedelta


# Create your models here.
class MyUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    # student_code = models.CharField(null=False, unique=True, max_length=10)
    # address = models.CharField(null=False, max_length=200)
    # phone_number = models.CharField(null=False, max_length=20)
    # avatar_url = models.ImageField(upload_to='uploads/%Y/%m')
    # specialization = models.CharField(null=False, max_length=200)
    
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    student_code = models.CharField(null=False, unique=True, max_length=10)
    address = models.TextField(null=False, max_length=200)
    phone_number = models.CharField(null=False, max_length=20)
    image = models.ImageField(upload_to='uploads/avatar/%Y/%m')
    specialization = models.CharField(null=False, max_length=200)
    course_year = models.CharField(null=False, max_length=10)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_cadres = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    @property
    def token(self):
        token = jwt.encode({
            'username': self.username, 'email': self.email, 'password': self.password, 'exp': datetime.utcnow() + timedelta(hours=24)},
            settings.SECRET_KEY, algorithm='HS256')
        return token
    
    # def get_image(self) :
    #     if self.image:
    #         return 'http://127.0.0.1:8000' + self.image.url
    #     return 'http://127.0.0.1:8000' + '/media/uploads/default.png'
    
class Profile(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    bod = models.DateField()
    gender = models.CharField(max_length=10, null=False)
    folk = models.CharField(max_length=100, null=False)
    dtut = models.CharField(max_length=100, null=False)
    religion = models.CharField(max_length=255, null=False)
    type_study = models.CharField(max_length=255, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Building(models.Model):
    building_name = models.CharField(null=False, unique=True, max_length=20)
    address = models.TextField(null=False, max_length=200)
    note = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/building/%Y/%m', null=True)
    
    def get_image(self) :
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return 'http://127.0.0.1:8000' + '/media/uploads/default.png'
    
class Room(models.Model):
    room_name = models.CharField(null=False, max_length=10)
    type_room = models.CharField(null=False, max_length=20)
    booked_number = models.IntegerField(default=0)
    max_number = models.IntegerField()
    month_cost = models.FloatField()
    note = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    
class Room_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
class BookingRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
class TypeLaundryService(models.Model):
    type_name = models.CharField(max_length=100)
    cost = models.FloatField()
    max_weight = models.IntegerField()
    note = models.TextField(max_length=255)
    
class BookingLaundryService(models.Model):
    type = models.ForeignKey(TypeLaundryService, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    isPay = models.BooleanField(default=False)
    
class StudyRoom(models.Model):
    room_name = models.CharField(null=False, max_length=50)
    number_seat = models.IntegerField()
    room_position = models.TextField(max_length=200)
    
class BookingStudyRoom(models.Model):
    student_code = models.CharField(max_length=20)
    seat = models.IntegerField()
    study_room = models.ForeignKey(StudyRoom, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateField(null=True)
    
class Reflect(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False)
    type_reflect = models.IntegerField()
    danger = models.BooleanField(default=False)
    note = models.TextField(max_length=255)
    isSeenByAdmin = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
class Payment(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    isPay = models.BooleanField(default=False)
    
class Notification(models.Model):
    content = models.TextField(max_length=500)
    isSeen = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


