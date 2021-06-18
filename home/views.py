from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from blog.models import Blog, Category, Images
from home.models import Settings, ContactFormu, ContactFormMessage


def index(request):
    settings = Settings.objects.get(pk=1)
    category = Category.objects.all()
    sliderdata = Blog.objects.all()[:5]
    dayblogs = Blog.objects.all()[:6]
    lastblogs = Blog.objects.all().order_by('-id')[:4]
    randomblogs = Blog.objects.all().order_by('?')[:9]
    populerblogs = Blog.objects.all()[:5]
    context = {'settings': settings,
               'sliderdata': sliderdata,
               'dayblogs': dayblogs,
               'category': category,
               'lastblogs': lastblogs,
               'randomblogs': randomblogs,
               'populerblogs': populerblogs,

               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    settings = Settings.objects.get(pk=1)
    category = Category.objects.all()

    context = {'settings': settings, 'category': category}
    return render(request, 'hakkimizda.html', context)


def referanslarımız(request):
    settings = Settings.objects.get(pk=1)
    category = Category.objects.all()

    context = {'settings': settings, 'category': category}
    return render(request, 'referanslarımız.html', context)


def iletisim(request):
    if request.method == 'POST':  # form post edildi ise
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kurma
            data.name = form.cleaned_data['name']  # formdan bilgi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # veri tabanına kaydet
            messages.success(request, "mesajınız başarı ile kaydedilmiştir")
            return HttpResponseRedirect('/iletisim')

    category = Category.objects.all()
    settings = Settings.objects.get(pk=1)
    form = ContactFormu()
    context = {'settings': settings, 'form': form, 'category': category}
    return render(request, 'iletisim.html', context)


def category_blogs(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    blogs = Blog.objects.filter(category_id=id)
    context = {
            'blogs': blogs,
            'category': category,
            'categorydata':categorydata,
               }

    return render(request, 'blogs.html', context)

def blog_detail(request,id,slug):
    category = Category.objects.all()
    image = Images.objects.filter(blog_id=id)
    blog = Blog.objects.get(pk=id)
    context = {
        'category': category,
        'blog':blog,
        'image':image,
    }
    return render(request, 'blog_detail.html',context)