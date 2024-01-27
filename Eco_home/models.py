from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

def home_directory_path(instance, filename):
    print(instance.id)
    return 'home_{0}/{1}'.format(instance.id, filename)

class Home(models.Model):
    city_location= models.CharField('City', max_length=20)
    home_location = models.CharField('Home Location',max_length=100)
    home_choice = (
        ('For Sale', 'For Sale'),
        ('For Rent', 'For Rent'),
    )
    home_type = models.CharField(max_length=30, choices=home_choice, null=True, blank=True )
    beds_rooms = models.IntegerField('Bed Rooms')
    bath_rooms = models.IntegerField('Bath Rooms')
    sqft = models.IntegerField('Square feet')
    price = models.IntegerField('Home Price')
    image = models.ImageField(upload_to=home_directory_path)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_location + "  /  " + self.home_location
    
    def get_name_url(self):
        home_url = self.city_location + " " + self.home_location + " " + str(self.id)
        home_url = slugify( home_url, allow_unicode=True) 
        return  home_url

class HomePicture(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, default="", null=True, blank=True)
    image = models.ImageField(null=True, default="", blank=True)

class TourRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tour_requests", default="")
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="tour_requests_home", default="", null=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    date = models.DateField(null=False)
    reservation_date = models.DateTimeField(auto_now_add=True)