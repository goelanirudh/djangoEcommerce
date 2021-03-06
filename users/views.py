from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import userRegisterForm


def register(request):
    if request.method=="POST":
        form=userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account has been created! You are now able to Log in')
            return redirect('/login')
    else:
        form=userRegisterForm()
    return render(request,'users/register.html',{'form':form})
