from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#class userProfile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    age = models.IntegerField()
#    occupation = models.CharField(max_length=100)

class BaseModel(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class authors(BaseModel):
    # _id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='images/')
    # created_timestamp = models.DateTimeField(auto_now_add=True)

class eBooks(BaseModel):
    # _id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    summary = models.TextField()
    website = models.URLField()
    # author = models.ForeignKey(authors, on_delete=models.DO_NOTHING)
    author = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images/')
    # created_timestamp = models.DateTimeField(auto_now_add=True)


class test(BaseModel):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')

class test2(BaseModel):
    name = models.CharField(max_length=100)

class test3(BaseModel):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(test2, on_delete=models.CASCADE)

class test4(BaseModel):
    img_model = models.ForeignKey(test, related_name='pictures', on_delete=models.CASCADE)
    pictures = models.ImageField(upload_to='images/')
