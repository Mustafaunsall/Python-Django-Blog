from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from content.models import Content, Menu, CImages


class ContentImagesInline(admin.TabularInline): #content sayfasında  resim galerisi ekleme 3 tane
    model = CImages
    extra = 3

class MenuContentInline(admin.TabularInline): #content sayfasında  resim galerisi ekleme 3 tane
    model = Content
    extra = 1


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','type','image_tag','status','create_at']  #content özelliklerini gösterme
    list_filter = ['status','type']
    inlines = [ContentImagesInline]
    prepopulated_fields = {'slug':('title',)}


class MenuAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title','status')
    list_filter = ['status']
    inlines = [MenuContentInline]

admin.site.register(Content,ContentAdmin)
admin.site.register(Menu,MenuAdmin)