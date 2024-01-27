from django.db import models
from django.utils.text import slugify
# Create your models here.
def blog_directory_path(instance, filename):
    print(instance.id)
    return 'blog/blog_{0}/{1}'.format(instance.id, filename)

class Blog(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True, default="")
    content = models.TextField(max_length=2500, blank=True, null=True, default="", serialize=False)
    image = models.ImageField(upload_to=blog_directory_path)
    author = models.CharField(max_length=100, blank=True, null=True, default="")
    date_bloged = models.DateTimeField(auto_now_add=True)

    def get_blog_url(self):
        home_url = slugify( self.title + " " + str(self.id), allow_unicode=True) 
        return  home_url