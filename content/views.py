from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from content.models import CommentForm, Comment


def index(request):
    return HttpResponse("Content Page")
@login_required(login_url='/login')
def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user

            data=Comment()
            data.user_id=current_user.id
            data.product_id=id
            data.subject=form.cleaned_data['subject']
            data.comment=form.cleaned_data['comment']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.Info(request,"Yorumunuz başarı ile gönderildi")

            return HttpResponseRedirect(url)

    messages.ERROR(request, "Yorumunuz kaydedilmedi")
    return HttpResponseRedirect(url)