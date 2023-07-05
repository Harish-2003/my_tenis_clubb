from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from members.models import Member
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
def members(request):
    template = loader.get_template('myfirst.html')
    mymembers=Member.objects.all()
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))
def details(request,id):
    template = loader.get_template('details.html')
    mymembers = Member.objects.get(id=id)
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
def loginpage(r):
    if not r.user.is_authenticated:
        if r.method == 'POST':
            usename = r.POST['username']
            password = r.POST['pwd']
            user = authenticate(username=usename, password=password)
            if user:
                login(r, user)
                messages.success(r, 'User login successful')
                return redirect('main/')
            else:
                messages.error(r, 'User not found')
                return render(r, 'login.html')
        else:
            return render(r, 'login.html')
    else:
        return redirect('main/')
def login(r):
    return render(r,'login.html')