from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(MPTTModel):

    STATUS = { #seçim

        ('True','Evet'),
        ('False','Hayır'),
    }
    parent = TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    link = models.CharField(blank=True,max_length=100)
    status = models.CharField(max_length=10,choices= STATUS) #açılan kutuda seçim olanı gelmesi için
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


class Content(models.Model):

    TYPE = { #seçim

        ('menu','menu'),
        ('haber','haber'),
        ('duyuru','duyuru'),
        ('etkinlik','etkinlik'),
    }
    STATUS = { #seçim

        ('True','Evet'),
        ('False','Hayır'),
    }
    menu = models.OneToOneField(Menu,null=True,blank=True,on_delete=models.CASCADE) #ilişkilendirme Menu ile
    type = models.CharField(choices=TYPE,max_length=10)
    title = models.CharField(blank=True,max_length=100)
    description = models.CharField(blank=True,max_length=255)
    keywords = models.CharField(blank=True,max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    detail = RichTextUploadingField()
    slug = models.SlugField(null=False,unique=True) #metinsel olarak çağırmak için
    status = models.CharField(max_length=10,choices= STATUS) #açılan kutuda seçim olanı gelmesi için
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title #dönderiyor

    def image_tag(self):    #resmi admin panelde göstermesi için
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('blog_detail',kwargs={'slug':self.slug})


class CImages(models.Model):
    content = models.ForeignKey(Content,on_delete=models.CASCADE) #ilişkilendirme category ile
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title #dönderiyor
    def image_tag(self):    #resmi admin panelde göstermesi için
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'