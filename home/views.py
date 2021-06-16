from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from home.models import Settings, ContactFormu, ContactFormMessage


def index(request):
    settings = Settings.objects.get(pk=1)

    context = {'settings': settings}
    return render(request, 'index.html', context)

def hakkimizda(request):
    settings = Settings.objects.get(pk=1)

    context = {'settings': settings}
    return render(request, 'hakkimizda.html', context)

def referanslarımız(request):
    settings = Settings.objects.get(pk=1)

    context = {'settings': settings,}
    return render(request, 'referanslarımız.html', context)

def iletisim(request):
    if request.method =='POST': #form post edildi ise
        form = ContactFormu(request.POST)
        if  form.is_valid():
            data = ContactFormMessage() #model ile bağlantı kurma
            data.name = form.cleaned_data['name']  #formdan bilgi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() #veri tabanına kaydet
            messages.success(request,"mesajınız başarı ile kaydedilmiştir")
            return HttpResponseRedirect('/iletisim')



    settings = Settings.objects.get(pk=1)
    form=ContactFormu()
    context = {'settings': settings,'form':form}
    return render(request, 'iletisim.html', context)