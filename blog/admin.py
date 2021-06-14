from django.contrib import admin

# Register your models here.
from blog.models import Category, Blog


class CategoryAdmin(admin.ModelAdmin):
    #fields = ['title', 'status'] ->categorydeki alanlar geliyor
    list_display = ['title', 'status']  #category özelliklerini gösterme
    list_filter = ['status']   # filtre ile listeleme

class BlogAdmin(admin.ModelAdmin):
    #fields = ['title', 'status'] ->categorydeki alanlar geliyor
    list_display = ['title','category', 'status']  #category özelliklerini gösterme
    list_filter = ['status','category']
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)