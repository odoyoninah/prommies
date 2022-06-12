from email.mime import image
from os import link
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prommies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    score = models.IntegerField(default=0)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    email = models.EmailField()
    my_file = models.FileField(upload_to='doc')

    def save_prommies(self):
        self.save()

    def delete_prommies(self):
        self.delete()

    def update_prommies(self, update):
        self.name = update.name
        self.description = update.description
        self.score = update.score
        self.link = update.link
        self.image = update.image
        self.email = update.email
        self.my_file = update.my_file
        self.save()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    bio = models.TextField(default='This is your bio')
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    project = models.ForeignKey(Prommies, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=100)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile_(self, new_profile):
        self.profile = new_profile
        self.save()

    def __str__(self):
        return self.user.username
