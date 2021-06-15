from django.contrib import admin

# Register your models here.
from blog.models import Category, Blog, Images

class BlogImagesInline(admin.TabularInline): #blog sayfasında  resim galerisi ekleme 3 tane
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    #fields = ['title', 'status'] ->categorydeki alanlar geliyor
    list_display = ['title', 'status','image_tag']  #category özelliklerini gösterme
    list_filter = ['status']   # filtre ile listeleme
    readonly_fields = ('image_tag',)

class BlogAdmin(admin.ModelAdmin):
    #fields = ['title', 'status'] ->categorydeki alanlar geliyor
    list_display = ['title','category','image_tag','status']  #category özelliklerini gösterme
    list_filter = ['status','category']
    inlines = [BlogImagesInline]
    readonly_fields = ('image_tag',)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'blog','image_tag']  #category özelliklerini gösterme
    readonly_fields = ('image_tag',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Images,ImagesAdmin)