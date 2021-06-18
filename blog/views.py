from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from blog.models import CommentForm, Comment


def index(request):
    return HttpResponse("Blog Page")


@login_required(login_url='/login')  # check login
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')  # son linki getir
    if request.method == 'POST':  # form post edildi ise
        form = CommentForm(request.POST)
        if form.is_valid():  # formdan elemanların tamamı geldi mi
            current_user = request.user  # kullanıcı oturum bilgilerine erişim

            data = Comment()  # model ile bağlantı kurma
            data.user_id = current_user.id  # oturumu açık olan kullanıcının idsiyle eşleştir
            data.blog_id = id  # gelen blog id ata
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')  # client computer ip address
            data.save()  # veri tabanına kaydet

            messages.success(request, "Yorumunuz başarı ile kaydedilmiştir")

            return HttpResponseRedirect(url)

    messages.warning(request, "yorumunuz kaydedilmedi.Lütfen kontrol ediniz")
    return HttpResponseRedirect(url)
