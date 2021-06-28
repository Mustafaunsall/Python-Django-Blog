from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Category
from home.models import UserProfile


def index(request):
    current_user = request.user  # kullanıcı oturum bilgilerine erişim
    profile = UserProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    context = {
         'category': category,
         'profile':profile,
               }
    return render(request, 'user_profile.html', context)
