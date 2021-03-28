from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text ="django kurulumu:python -m pip install -e django <br> proje oluşturma: djanggo-admin startproject mysite <br>  App ekleme:python manage.py startapp polls"
    context = {'text': text}
    return render(request, 'index.html', context)