from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    #path('addcomment/<int:id>', views.addcomment,name='addcomment'),
    path('update/', views.user_update,name='user_update'),
    path('password/', views.change_password,name='change_password'),

    path('comments/', views.comments,name='comments'),
    path('deletecomment/<int:id>', views.deletecomment,name='deletecomment'),

    path('contents/', views.contents,name='contents'),
    path('addcontent/', views.addcontent,name='addcontent'),
    path('contentedit/<int:id>', views.contentedit,name='contentedit'),
    path('contentdelete/<int:id>', views.contentdelete,name='contentdelete'),
    path('contentaddimage/<int:id>', views.contentaddimage,name='contentaddimage'),

    path('blogs/', views.blogs,name='blogs'),
    path('addblog/', views.addblog,name='addblog'),
    path('blogedit/<int:id>', views.blogedit,name='blogedit'),
    path('blogdelete/<int:id>', views.blogdelete,name='blogdelete'),
    path('blogaddimage/<int:id>', views.blogaddimage,name='blogaddimage'),
]