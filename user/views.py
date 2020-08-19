from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from content.models import Category
from home.models import UserProfili


def index(request):
    category=Category.objects.all()
    current_user=request.user
    profile=UserProfili.objects.get(user_id=current_user.id)
    context={'category':category,
             'profile':profile,
             }
    return render(request,'user_profile.html',context)