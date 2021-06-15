from django.db import models

# Create your models here.

class Category(models.Model):

    STATUS = { #seçim

        ('True','Evet'),
        ('False','Hayır'),
    }
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10,choices= STATUS) #açılan kutuda seçim olanı gelmesi için
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    slug = models.SlugField() #metinsel olarak çağırmak için
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title #dönderiyor

class Blog(models.Model):

    STATUS = { #seçim

        ('True','Evet'),
        ('False','Hayır'),
    }
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10,choices= STATUS) #açılan kutuda seçim olanı gelmesi için
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #ilişkilendirme category ile
    detail = models.TextField()
    slug = models.SlugField() #metinsel olarak çağırmak için
    file = models.FileField(blank=True,upload_to='files/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title #dönderiyor

class Images(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE) #ilişkilendirme category ile
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title #dönderiyor