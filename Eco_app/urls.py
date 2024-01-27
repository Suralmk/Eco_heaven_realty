from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('company/', company, name='company'),


    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),

    # #password reset urls
    path('reset-password/', reset_password, name='reset_password'),
    path('email-sent/', email_sent_confirmation, name='email-sent'),
    path('create-password/<slug:token>/', create_password, name='create-password'),
    path('reset-complete/', reset_complete, name='reset-complete'),

    # #Authenticated user profile urls
    # # path('change-password/', views.change_password, name='change_password'),
    # # path('change-email/', views.change_email, name='change_email'),
    # # path('change-username/', views.change_username, name='change_username'),

    # # Searching a post every one can search
    # # no need to login, signup, be an admin
    # # path('searched-post/', views.search_post, name='searched-post'),
    # path("admin-staff/", eco_admin, name='admin-staff')
    path("not-found/", not_found, name='not-found')
]