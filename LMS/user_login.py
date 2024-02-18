from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from home.EmailBackend import EmailBackend
from django.contrib.auth import login,logout


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

def do_login(request):
   if request.method=='POST':
      email=request.POST.get('email')
      password=request.POST.get('password')
      user=EmailBackend.authenticate(request,email,password)

      if user is not None:
         login(request,user)
         return redirect('home:index')
      else:
         
         messages.error(request,'Invalid credentials')
         return redirect('login')
      
def logout_user(request):
   logout(request)
   return redirect('home:index')

def profile_view(request):
   return render(request,'registration/profile.html')

def profile_update(request):
   if request.method == 'POST':
      username=request.POST.get('username')
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      email=request.POST.get('email')
      password= request.POST.get('password')

      user_id=request.user.id

      user= User.objects.get(id=user_id)
      user.first_name= first_name
      user.last_name= last_name
      user.username= username
      user.email= email

      if password != None and password !="":
         user.set_password(password)
      user.save()
      messages.success(request,'Profile is successfully updated!')

   return redirect('profile_view')
   
   