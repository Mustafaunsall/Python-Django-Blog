"""blogd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('blog/', include('blog.urls')), #blog app urli tanıt
    path('', include('home.urls')), #home app urli tanıt
    path('home/', include('home.urls')), #home app urli tanıt
    path('user/', include('user.urls')), #user app urli tanıt
    path('content/', include('content.urls')), #content app urli tanıt
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),


    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('referanslarimiz/', views.referanslarimiz, name='referanslarimiz'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('faq/', views.faq, name='faq'),
    path('error/', views.error, name='error'),

    path('category/<int:id>/<slug:slug>/', views.category_blogs,name='category_blogs'),
    path('blog/<int:id>/<slug:slug>/', views.blog_detail,name='blog_detail'),
    path('content/<int:id>/<slug:slug>/', views.content_detail,name='content_detail'),
    path('menu/<int:id>/', views.menu,name='menu'),

    path('search/', views.blog_search,name='blog_search'),
    path('search_auto/', views.blog_search_auto,name='blog_search_auto'),

    path('logout/', views.logout_view,name='logout_view'),
    path('login/', views.login_view,name='login_view'),
    path('signup/', views.signup_view,name='signup_view'),




]
if settings.DEBUG: #new resimleri göstermek için yol
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
