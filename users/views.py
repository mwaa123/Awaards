from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.db.models.signals import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            
        return redirect('')
    else:
        form = UserRegisterForm()
    return render(request, 'find/register.html', {'form': form})

def register(request):
    form =UserCreationForm()
    return render(request,'users/register.html',{'form':form})

