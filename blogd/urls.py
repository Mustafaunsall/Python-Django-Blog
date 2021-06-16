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
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('referanslarımız/', views.referanslarımız, name='referanslarımız'),
    path('iletişim/', views.iletişim, name='iletişim'),
    path('', include('home.urls')), #home app urli tanıt
    path('home/', include('home.urls')), #home app urli tanıt
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG: #new resimleri göstermek için yol
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
