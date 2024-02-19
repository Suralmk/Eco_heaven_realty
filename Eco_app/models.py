from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
  def create_user (self, email, first_name=None, last_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
      if not email:
          raise ValueError("User must have email")
    #   if not password:
    #       raise ValueError("User must have password")
    #   if not first_name:
    #       raise ValueError("User must have first_name")
    #   if not last_name:
    #       raise ValueError("User must have last_name")

      

      email = self.normalize_email(email)
      user = self.model( 
          email=email,
      )
      user.set_password(password)
      user.first_name=first_name
      user.last_name=last_name
      user.active = is_active
      user.staff = is_staff
      user.admin = is_admin
      user.save()
      return user
  
  def create_staffuser(self, email, first_name=None, last_name=None, password=None):
      if not email:
          raise ValueError("User must have email")
      if not password:
          raise ValueError("User must have password")
    #   if not first_name:
    #       raise ValueError("User must have first_name")
    #   if not last_name:
    #       raise ValueError("User must have last_name")
      
      user = self.create_user(
          email, 
          first_name,
          last_name,
          password=password,
          is_staff=True
      )
      return user
  def create_superuser(self, email, first_name=None ,last_name=None, password=None): 
      if not email:
          raise ValueError("User must have email")
      if not password:
          raise ValueError("User must have password")
      
      user = self.create_user(
          email,
          first_name,
          last_name,
          password=password,
          is_staff=True,
          is_admin=True
      )
      return user

class User(AbstractBaseUser, PermissionsMixin):
    email =   models.EmailField(unique=True, null=False, max_length=255, default=None)
    first_name = models.CharField(max_length=150, blank=True,null=True, default="unknown")
    last_name = models.CharField(max_length=150, blank=True, null=True, default="user")
    active =  models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects  = UserManager()

    def __str__(self):
        return self.email

    
    def get_short_name(self):
        return self.first_name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
      
class CustomerContact(models.Model):
    customer_enquiry = (
        ('BUY', 'Buy a House'),
        ('RENT', 'Rent a House'),
        ('VISIT', 'Visit a House'),
        ('AGENT', 'Contact Agent'),
        ('INFORMATION', 'Information About Locations'), 
    )
    full_name = models.CharField(max_length=100, default="", blank=True)
    phone_number= models.IntegerField()
    email = models.EmailField()
    enquiry = models.CharField(max_length=50, null=True, blank=True, default="", choices=customer_enquiry)
    message = models.TextField(max_length=400, null=True, blank=True, default="" )


    def __str__(self):
        return self.full_name

# import uuid
# import time
# class ResetRequest(models.Model):
#     email = models.EmailField(default="", blank=True, null=True, max_length=150)
#     token = models.SlugField(default=uuid.uuid4, null=True, blank=True)
#     timestamp = models.DateTimeField()


#     def manage_token(self, id):
#         reset_request = self.objects.get(id=id)
#         if time.time - reset_request.timestamp >= 3:
#             reset_request.delete()

