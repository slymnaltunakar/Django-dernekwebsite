from django.core.checks import messages
from django.core.mail import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from content.models import Product, Category
from home.models import Setting, ContactFormumuz, ContactForm


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:3]
    category = Category.objects.all()
    lasthaber= Product.objects.all().order_by('-id')[:6]

    context = {'setting': setting, 'page': 'home', 'sliderdata':sliderdata ,'category': category, 'lasthaber':lasthaber }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'hakkimizda','category': category}
    return render(request, 'hakkimizda.html', context)


def bagiscilar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'bagiscilarimiz','category': category}
    return render(request, 'bagiscilarimiz.html', context)

def iletisim(request):

    if request.method == 'POST':
        form = ContactFormumuz(request.POST)
        if form.is_valid():
            data = ContactForm()
            data.name =form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, "Mesajınız başarılı bir şekilde gönderilmiştir. Teşekkürler")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm()
    context = {'setting': setting, 'page': 'iletisim','category': category}
    return render(request, 'iletisim.html', context)


def category_products(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products': products,'category': category, 'slug': slug}
    return render(request, 'productss.html',context)