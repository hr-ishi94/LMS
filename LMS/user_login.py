from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
   if request.method=='POST':
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')

      if User.objects.filter(username=username).exists():
         messages.warning(request,'Username already exists!')
         return redirect('register')
      
      if User.objects.filter(email=email).exists():
         messages.warning(request,'Email already exists!')
         return redirect('register')
      
      user=User(
         username=username,
         email=email
         )
      user.set_password(password)
      user.save()
      messages.success(request,'Registration Successful. Please Login!')
      return redirect('login')

   return render(request,'registration/register.html')