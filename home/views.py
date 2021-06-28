import json

from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from blog.models import Blog, Category, Images, Comment
from home.forms import SearchForm, SignUpForm
from home.models import Settings, ContactFormu, ContactFormMessage, UserProfile


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


def category_blogs(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    blogs = Blog.objects.filter(category_id=id)
    context = {
        'blogs': blogs,
        'category': category,
        'categorydata': categorydata,
    }

    return render(request, 'blogs.html', context)


def blog_detail(request, id, slug):
    category = Category.objects.all()
    image = Images.objects.filter(blog_id=id)
    blog = Blog.objects.get(pk=id)
    comments = Comment.objects.filter(blog_id=id, status='True')
    context = {
        'category': category,
        'blog': blog,
        'image': image,
        'comments': comments,

    }
    return render(request, 'blog_detail.html', context)


def blog_search(request):
    if request.method == 'POST':  # form post edildi ise
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']  # formdan bilgi al
            blogs = Blog.objects.filter(title__icontains=query)  # select * from blog where title like %query%

            context = {
                'category': category,
                'blogs': blogs,
            }

            return render(request, 'blogs_search.html', context)

    return HttpResponseRedirect('/')


def blog_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        blog = Blog.objects.filter(title__icontains=q)
        results = []
        for rs in blog:
            blog_json = {}
            blog_json = rs.title
            results.append(blog_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':  # form post edildi ise
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatası! Kullanıcı adı veya sifre yanlış")
            return HttpResponseRedirect('/login')
            # Return an 'invalid login' error message.

    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login.html',context)

def signup_view(request):
    if request.method == 'POST':  # form post edildi ise
        form = SignUpForm(request.POST)
        if form.is_valid(): #control
            form.save()  #kayıt yapıldı ekstra şeyler kaydetmeyeceksek böyle kaydedilir
            username = form.cleaned_data.get('username') #login işlemi
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Redirect to a success page.
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'signup.html',context)

