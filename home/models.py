from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


class Settings(models.Model):
    STATUS = {  # seçim

        ('True', 'Evet'),
        ('False', 'Hayır'),
    }
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    company = models.CharField(blank=True, max_length=100)
    adress = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=100)
    smtpemail = models.CharField(blank=True, max_length=100)
    smtppassword = models.CharField(blank=True, max_length=100)
    smtpport = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    twitter = models.CharField(blank=True, max_length=100)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title  # dönderiyor


class ContactFormMessage(models.Model):
    STATUS = {  # seçim

        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    }
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=255)
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  # dönderiyor


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {



           'name' : TextInput(attrs={'class': 'form-control', 'placeholder': 'your name & surname'}),
           'email' :  TextInput(attrs={'class': 'form-control', 'placeholder': 'your email'}),
           'subject' :  TextInput(attrs={'class': 'form-control', 'placeholder': 'subject'}),
           'message' : Textarea(attrs={'class': 'form-control', 'placeholder': 'message', 'rows': '10'}),


        }

class UserProfile(models.Model):  #user profil resim işlemleri
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=15)
    address = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username  # dönderiyor
    def user_name(self):
        return '[' +self.user.username + ']  ' +self.user.first_name + '  ' +self.user.last_name

    def image_tag(self):    #resmi admin panelde göstermesi için
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city','country','image']

