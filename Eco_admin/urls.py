from django.urls import path
from .views import *



urlpatterns = [
      path('', staff, name='staff'), # Done 

      # Users urls
      path('users-list/' ,users_list, name='users-list'), # Done
      path('users-list/<int:id>/' ,user_detail, name='users-detail'),
      path('users-list/<int:id>/delete/' ,users_delete, name='users-delete'), # Done
      path('users-list/staff-users-add/' ,staff_users_add, name='staff-users-add'), # Done with validation
      

      # Homes Urls 
      path('home-list/' ,home, name='home-list'), # done
      path('home-list/create/' ,home_create, name='home-create'), # Done 
      path('home-list/<int:id>/' ,home_detail, name='admin-home-detail'), # Done 
      path('home-list/<int:id>/add-more-images/' ,home_detail_add_images, name='home-detail-add-images'), # Done
      path('home-list/<int:id>/<int:imgId>/delete-home-image/' ,delete_home_image, name='delete-home-image'), # Done
      path('home-list/<int:id>/update/' ,home_update, name='home-update'),# -----------
      path('home-list/<int:id>/delete/' ,home_delete, name='home-delete'), # Done 

      # Blog Urls 
      path('blog-list/' ,blog_list, name='admin-blog-list'), # Done
      path('blog-list/create/' ,blog_create, name='admin-blog-create'), # Done 
      path('blog-list/<int:id>/' ,blog_detail, name='admin-blog-detail'), # Done 
      path('blog-list/<int:id>/update/' ,blog_update, name='admin-blog-update'),
      path('blog-list/<int:id>/delete/' ,blog_delete, name='admin-blog-delete'), # Done

      # Tour Rewquests Urls
      path('tour-requests/', tour_requests_list, name="tour-requests-list"),
      path('tour-requests/<int:id>/', tour_requests_delete, name="tour-requests-detail"),
      path('tour-requests/<int:id>/delete/', tour_requests_delete, name="tour-requests-delete"),
 
      # Messages Urls 
      path('messages/', messages_list, name="messages-list"),
      path('messages/<int:id>/', messages_delete, name="messages-detail"),
      path('messages/<int:id>/delete/', messages_delete, name="messages-delete"),
]