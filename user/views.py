from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from content.models import Category
from home.models import UserProfili
from user.forms import UserUpdateForm, ProfileUpdateForm


@login_required(login_url='/login')
def index(request):
    category=Category.objects.all()
    current_user=request.user
    profile=UserProfili.objects.get(user_id=current_user.id)
    context={'category':category,
             'profile':profile,
             }
    return render(request,'user_profile.html',context)


@login_required(login_url='/login')
def user_update(request):
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user) #request user is user session data

        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofili)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return  redirect('/user')

    else:
        category= Category.objects.all()
        user_form=UserUpdateForm(instance=request.user)# user form user ile ilişki kuracak
        profile_form=ProfileUpdateForm(instance=request.user.userprofili)

        context={
            'category':category,
            'user_form':user_form,
            'profile_form':profile_form,
        }
        return  render(request,'user_update.html',context)

@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            return  redirect('change_password')
        else:
            messages.error(request,'Please correct the error below.<br>'+str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category=Category.objects.all()
        form=PasswordChangeForm(request.user)
        return render(request,'change_password.html',{
            'form':form,'category':category
        })