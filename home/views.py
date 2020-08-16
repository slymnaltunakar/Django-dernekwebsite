from django.core.checks import messages
from django.core.mail import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from content.models import Product
from home.models import Setting, ContactFormumuz, ContactForm


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:3]

    context = {'setting': setting, 'page': 'home', 'sliderdata':sliderdata }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def bagiscilar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'bagiscilarimiz'}
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
    form = ContactForm()
    context = {'setting': setting, 'page': 'iletisim'}
    return render(request, 'iletisim.html', context)