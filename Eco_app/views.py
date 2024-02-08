from django.shortcuts import render, redirect
from django.contrib import messages
from  django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from Eco_home.models import Home
from . models import CustomerContact
import time, uuid
from django.contrib.auth.decorators import login_required

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import  force_str, smart_bytes, smart_str
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .helpers import Util
# from . models import ResetRequest
# Create your views here.
User = get_user_model()

def company (request):
     return render (request, "Eco_app/company.html")

def index(request):
    homes = Home.objects.all().order_by('?')
    if homes:
         context = {
              'homes' : homes
         }
    else:
         context = {}


    if request.method == "POST":
         full_name = request.POST['full-name']
         phone_number = request.POST['phone-number'] 
         email = request.POST['email'] 
         enquiry = request.POST['enquiry']
         message = request.POST["message"]

         try:
              contact_req = CustomerContact.objects.create(
                        full_name=full_name, phone_number=phone_number,
                         email=email, enquiry=enquiry, message=message
                        )
              contact_req.save()
         except Exception as e:
              print(e)

    return render(request, "Eco_app/index.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        # storing the values entered by the user in a variable.
        email = request.POST['email']
        password = request.POST['password']
        auth_user = authenticate(request, email=email, password=password)
        if email == "" or password == "":
             messages.error(request, "Please enter all required fields!")
        elif auth_user == None:
            messages.error(request, "User not found!")
        elif auth_user is not None:
            auth_login(request, auth_user)
            return redirect('index')
        else:
            return redirect('index')
    return render(request, 'Eco_app/login.html')

def signup(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if first_name == "" or last_name == "" or email == "" or password == "" :
             messages.error(request, 'Please enter all the required fields!')   
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email was already Taken!')
           
        else:
            #send welcome email here before regestering the user
            email_context = {
                "first_name": first_name
            }
            subject = 'Welcome to Eco Heaven Realty'
            user_email = [email]
            # send_welcome_email(request, subject, email_context, user_email )

            user = User.objects.create_user(
                                            first_name=first_name,
                                            last_name=last_name,
                                            password=password,
                                            email=email )
            messages.success(request, 'Succesfully registered please login!')
            return redirect("login")
      
    return render(request, 'Eco_app/signup.html')

def logout(request):
    auth_logout(request)
    return redirect('index')



# Password reset
def reset_password(request):
    if request.method == 'POST':
          email = request.POST['email']

          if User.objects.filter(email=email).exists():
               user=User.objects.get(email=email)
               uidb64=urlsafe_base64_encode(smart_bytes(user.id))
               token = PasswordResetTokenGenerator().make_token(user)
               current_site = get_current_site(request=request).domain
               relative_link = reverse('create-password', kwargs={'uidb64' : uidb64, 'token':token})
               absurl = f'http://{current_site}{relative_link}'
               email_body = f"Hello {user.first_name} \n\n Use this link bellow to reset your password \n {absurl}"
               data = {
                         'email_body' : email_body, 
                         'to_email': user.email,
                         'email_subject' : 'Password Reset Request'
                         }
               Util.send_email(data)
               return redirect('email-sent')
          else:
               messages.error(request, "Email not found")
    return render( request, 'Eco_app/auth/reset_password.html')

def email_sent_confirmation(request):
     
     return render(request, 'Eco_app/auth/email_sent_confirmation.html')

def create_password(request,uidb64, token):
     if request.method == "GET":
          try:
               id = smart_str(urlsafe_base64_decode(uidb64))
               user = User.objects.get(id=id)

               if not PasswordResetTokenGenerator().check_token(user, token=token):
                    return redirect('not-found')
          except Exception as e:
               return redirect("not-found")
     if request.method == "POST":
               password = request.POST['new-password']
               print(password)
     return render(request, 'Eco_app/auth/create_new_password.html')

def reset_complete(request):
     return render(request, 'Eco_app/auth/reset_complete.html')

def not_found(request):
     return render(request, "Eco_app/not_found.html")



# Authentication update views
@login_required
def change_email (request):
     if request.method == 'POST':
          new_email = request.POST['new-email']

          try:
               new_user = User.objects.filter(email=request.user).update(email=new_email)
               new_user.save()
          except Exception as e:
               print(e)

     return render(request, 'Eco_app/auth_change/change_email.html')

@login_required
def change_name (request):
     current_user = User.objects.get(email=request.user)
     if request.method == 'POST':
          new_first_name = request.POST['new-first-name']
          new_last_name = request.POST['new-last-name']

          try:
               new_user = User.objects.filter(email=request.user).update(first_name=new_first_name, last_name=new_last_name)
               new_user.save()
               messages.success(request, "Name edited succesfully")
          except Exception as e:
               print(e)
     

     return render(request, 'Eco_app/auth_change/change_name.html', {"user": current_user})

@login_required
def change_password(request):
     current_user = User.objects.get(email=request.user)
     if request.method == 'POST':
          new_password = request.POST['new-password']
          try:
               current_user.set_password(new_password)
               current_user.save()
               
               
          except Exception as e:
               print(e)
          
     return render(request, 'Eco_app/auth_change/change_password.html')


