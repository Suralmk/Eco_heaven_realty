from django.shortcuts import render, redirect
from django.http import HttpResponse
from Eco_home.models import Home, HomePicture, TourRequest
from Eco_blog . models import Blog
from django.contrib.auth import get_user_model
from django.contrib import messages
from Eco_app.models import CustomerContact
from Eco_home.models import TourRequest

# Create your views here.
User = get_user_model()


# Admin  staff View
def staff (request):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found") 
    else:
        return render(request, "Eco_admin/staff.html")


# Admin User Views
def users_list (request):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    users = User.objects.all()
    context = {
        "users" : users
    }
    return render(request, "Eco_admin/User/users_list.html", context)

def staff_users_add(request):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    if request.method == 'POST':
        staff_first_name = request.POST["staff_first_name"]
        staff_last_name = request.POST["staff_last_name"]
        staff_email = request.POST["staff_email"]
        staff_password = request.POST["staff_password"]

        print()
        if staff_first_name == "" or staff_last_name == "" or staff_email == "" or staff_password == "" :
             messages.error(request, 'Please enter all the required fields!')   
        elif User.objects.filter(email=staff_email).exists():
            messages.error(request, 'Email was already Taken!')

        try:
            staff_user = User.objects.create(first_name=staff_first_name, last_name=staff_last_name, 
                                            email=staff_email, password=staff_password, staff=True)
            staff_user.save()
        except Exception as e:
            print(e)
        
    return render(request, "Eco_admin/User/add_staff.html")

def user_detail (request, id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    user = User.objects.get(id=id)
    context = {
        "user" : user
    }
    return render(request, "Eco_admin/User/user_detail.html", context)

def users_delete (request, id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    user = User.objects.get(id=id)

    if  user.is_staff or user.is_admin:
        messages.error (request, "Staff members can not be deleted!")
        return redirect("users-list") 
    else:
        messages.success (request, f"{user.first_name} {user.last_name} id deleted")
        user.delete()
        return redirect("users-list")


# Admin Home Views
def home(request):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    homes = Home.objects.all()
    context = {
        "homes" : homes
    }
    return render(request, "Eco_admin/Home/home_list.html", context)

def home_create(request):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    

    if request.method == "POST":
        city_location = request.POST["city_location"]
        home_location = request.POST["home_location"]
        bath_rooms = request.POST["bath_rooms"]
        bed_rooms = request.POST["bed_rooms"]
        sqft = request.POST["sqft"]
        price = request.POST["price"]
        home_type = request.POST['home_type']
        description = request.POST['home_description']
        image = request.FILES['image']


        try:
            home = Home.objects.create( city_location=city_location,home_location=home_location,
                                    home_type=home_type, bath_rooms=bath_rooms, beds_rooms=bed_rooms,
                                    sqft=sqft, price=price,description=description, image=image
                                   )      
            home.save()
        except Exception as e:
            print(e)

        homepic = HomePicture.objects.create(home=home, image=image)
        homepic.save()
        return redirect("home-list")
    return render(request, "Eco_admin/Home/home_create.html")

def home_detail(request,id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    home = Home.objects.get(id=id)
    homepics = HomePicture.objects.filter(home=home).all()

    context = {
        "home": home, 
        "homepics" : homepics
    }
    return render(request, "Eco_admin/Home/home_detail.html", context)

def home_detail_add_images(request, id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    home = Home.objects.get(id=id)
    if request.method == "POST":
        try:
            images = request.FILES.getlist("home_images")
            for image in images:
                homepic = HomePicture.objects.create(
                    home=home,
                    image=image
                )
            homepic.save() 
            return redirect("admin-home-detail", id )
        except Exception as e:
            print(e)
        
    return render(request, "Eco_admin/Home/home_add_more_images.html")

def delete_home_image(request, id, imgId):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    homepic = HomePicture.objects.filter(id=imgId).delete()
    return redirect("admin-home-detail", id)

def home_update(request, id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    home = Home.objects.get(id=id)
 
    
    if request.method == "POST":
        city_location = request.POST["city_location"]
        home_location = request.POST["home_location"]
        bath_rooms = request.POST["bath_rooms"]
        bed_rooms = request.POST["bed_rooms"]
        sqft = request.POST["sqft"]
        price = request.POST["price"]
        home_type = request.POST['home_type']
        home_image = request.FILES['image']

        try:
            if home is not None:
                home.city_location = city_location
                home.home_location= home_location
                home.home_type= home_type
                home.bath_rooms= bath_rooms
                home.beds_rooms= bed_rooms
                home.sqft= sqft
                home.price = price
                if home_image:
                    home.image = home_image 
                else:
                    home.image = home.image
                home.save()
        except Exception as e:
            print(e)

        
        return redirect("home-list")
    return render(request, "Eco_admin/Home/home_update.html", {"home" : home})

def home_delete(request, id):
        if not request.user.is_authenticated:
            return redirect ("not-found")
        elif not request.user.is_staff:
            return redirect("not-found")

        home = Home.objects.filter(id=id).delete()
        return redirect("home-list")

# Admin Blog Views
def blog_list(request):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    blogs = Blog.objects.all()

    context = {
        "blogs" : blogs
    }
    return render(request, "Eco_admin/Blog/blog_list.html", context)

def blog_create(request):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    if request.method == "POST":
        title = request.POST["blog_title"]
        content = request.POST["blog_content"]
        image = request.FILES["blog_image"]
        author = request.POST["blog_author"]

        try:
            blog = Blog.objects.create(title=title, content=content, image=image, author=author)
            blog.save()
        except Exception as e :
            print(e)

    return render(request, "Eco_admin/Blog/blog_create.html")

def blog_detail(request, id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")

    blog = Blog.objects.filter(id =id).first()

    context = {
        "blog" :blog
    }
    return render(request, "Eco_admin/Blog/blog_detail.html", context)

def blog_update(request,  id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    blog = Blog.objects.get(id=id) or None

    if request.method== "POST":
        title = request.POST["blog_title"]
        content = request.POST["blog_content"]
        image = request.FILES["blog_image"]
        author = request.POST["blog_author"]

        try:
            if blog is not None:
                blog.title = title
                blog.content = content
                blog.image= image
                blog.author=author

                blog.save()
        except Exception as e:
            print(e)
    return render(request, "Eco_admin/Blog/blog_update.html", {"blog" : blog})

def blog_delete(request, id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    blog = Blog.objects.filter(id=id).delete()
    return redirect("admin-blog-list")

# Tour Requests Views

def tour_requests_list(request):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    tour_requests = TourRequest.objects.all()


    context = {
        "tour_requests" :tour_requests
    }
    return render(request,"Eco_admin/TourRequests/tour_requests_list.html", context )

def tour_requests_delete(request, id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    tour_request = TourRequest.objects.filter(id=id).delete()
    return redirect("tour-requests-list")

# Customer Contact Messages Views 
def messages_list(request):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    contact_messages = CustomerContact.objects.all()
    
    context = {
        "contact_messages" : contact_messages
    }
    return render(request, "Eco_admin/Message/messages_list.html", context)

def messages_delete(request, id):
    if not request.user.is_authenticated:
        return redirect ("not-found")
    elif not request.user.is_staff:
        return redirect("not-found")
    
    message = CustomerContact.objects.filter(id=id).delete()
    return redirect("messages-list")
