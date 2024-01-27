from django.urls import path
from . views import *

urlpatterns = [
    path ('', blog, name="blog"),
    path ('blog-detail/<slug:blogname>/<int:id>/', eco_blog_detail, name="blog-detail")
]