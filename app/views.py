from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail

from app.form import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')


def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}

    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            send_mail('REgsitration',
                        'thank u for regsitration',
                        'krish766778@gmail.com',
                        [MUFDO.email],
                        fail_silently=False,
                        
            )
            return HttpResponse('Registration is Successfull')
        else:
            return HttpResponse('Invalid data')

    return render(request,'registration.html',d)


def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']

        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Credentials')


    return render(request,'user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile_display(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    return render(request,'profile_display.html',{'UO':UO,'PO':PO})


@login_required
def change_password(request):
    if request.method=='POST':
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        nw=request.POST['nw']
        UO.set_password(nw)
        UO.save()
        return HttpResponse('Password Changed Successfully')

    return render(request,'change_password.html')
    
def reset_pass(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']

        LUO=User.objects.filter(username=un)
        if LUO:
            UO=LUO[0]
            UO.set_password(pw)
            UO.save()
            return HttpResponse('Password reset is done')
        else:
            return HttpResponse('username is not avaialble in DB')
    return render(request,'reset_pass.html')
    


    