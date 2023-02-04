from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 255)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    counted_views = models.IntegerField(default= 0)
    login_require = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now= True)
    published_date = models.DateTimeField(null=True)


    class Meta:
        ordering = ['-published_date']


    def __str__(self):
        return "{}-{}".format(self.title, self.counted_views)


    def get_absolute_url(self):
        return reverse ('blog:single_blog', kwargs={'pid':self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email= models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now= True)
    approved = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
