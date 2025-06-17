from django.db import models

# Create your models here.

class Tag(models.Model):
    Caption = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Caption}'

class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80,blank=False,null=False,unique=True)

    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return self.fullname()



class Post(models.Model):
    title = models.CharField(max_length=80)
    Excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    Date = models.DateField(auto_now_add=True)
    slug = models.SlugField(db_index=True,unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    tags = models.ManyToManyField(Tag)
