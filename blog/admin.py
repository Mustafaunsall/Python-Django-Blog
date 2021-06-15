from django.contrib import admin

# Register your models here.
from blog.models import Category, Blog, Images

class BlogImagesInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    #fields = ['title', 'status'] ->categorydeki alanlar geliyor
    list_display = ['title', 'status']  #category özelliklerini gösterme
    list_filter = ['status']   # filtre ile listeleme

class BlogAdmin(admin.ModelAdmin):
    #fields = ['title', 'status'] ->categorydeki alanlar geliyor
    list_display = ['title','category', 'status']  #category özelliklerini gösterme
    list_filter = ['status','category']
    inlines = [BlogImagesInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'blog','image']  #category özelliklerini gösterme
    list_filter = ['title','blog']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Images,ImagesAdmin)