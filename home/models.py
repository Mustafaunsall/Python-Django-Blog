from django.db import models

# Create your models here.


class Settings(models.Model):
    STATUS = { #seçim

        ('True','Evet'),
        ('False','Hayır'),
    }
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    company = models.CharField(blank=True,max_length=100)
    adress = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=100)
    smtpemail = models.CharField(blank=True,max_length=100)
    smtppassword = models.CharField(blank=True,max_length=100)
    smtpport = models.CharField(blank=True,max_length=100)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=100)
    instagram = models.CharField(blank=True,max_length=100)
    twitter = models.CharField(blank=True,max_length=100)
    aboutus = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    references = models.TextField(blank=True)
    status = models.CharField(max_length=10,choices= STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title #dönderiyor
