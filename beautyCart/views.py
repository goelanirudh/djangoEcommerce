from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html')


def handleSingup(request):
    if request.method=='POST':
        # Get the post parameters
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for erronous input
        #
        # Create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        # messages.success(request,'Your account has been created')
        return redirect('/shop')

    else:
        return HttpResponse('404- Not Found')