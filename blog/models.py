from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):

    STATUS = { #seçim

        ('True','Evet'),
        ('False','Hayır'),
    }
    title = models.CharField(max_length=30)
    description = models.CharField(blank=True,max_length=255)
    keywords = models.CharField(blank=True,max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10,choices= STATUS) #açılan kutuda seçim olanı gelmesi için
    parent = TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    slug = models.SlugField() #metinsel olarak çağırmak için
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
       # level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]  # admindeki alt categoryler için
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path[::-1])




    def image_tag(self):    #resmi admin panelde göstermesi için
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Blog(models.Model):

    STATUS = { #seçim

        ('True','Evet'),
        ('False','Hayır'),
    }
    title = models.CharField(blank=True,max_length=100)
    description = models.CharField(blank=True,max_length=255)
    keywords = models.CharField(blank=True,max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10,choices= STATUS) #açılan kutuda seçim olanı gelmesi için
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #ilişkilendirme category ile
    user = models.ForeignKey(User,on_delete=models.CASCADE) #ilişkilendirme user ile
    detail = RichTextUploadingField()
    slug = models.SlugField() #metinsel olarak çağırmak için
    file = models.FileField(blank=True,upload_to='files/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title #dönderiyor

    def image_tag(self):    #resmi admin panelde göstermesi için
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Images(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE) #ilişkilendirme category ile
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title #dönderiyor
    def image_tag(self):    #resmi admin panelde göstermesi için
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Comment(models.Model):
    STATUS = { #seçim
        ('New','Yeni'),
        ('True','Evet'),
        ('False','Hayır'),
    }
    subject = models.CharField(blank=True,max_length=50)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE) #ilişkilendirme category ile
    user = models.ForeignKey(User,on_delete=models.CASCADE) #ilişkilendirme user ile
    rate = models.IntegerField(blank=True)
    comment = models.TextField(blank=True,max_length=200)
    status = models.CharField(max_length=10,choices= STATUS,default='New') #açılan kutuda seçim olanı gelmesi için
    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject #dönderiyor

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields =['subject','comment','rate']