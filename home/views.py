from django.shortcuts import render
from .models import Categories

def index(request):
    category= Categories.objects.all().order_by('id')[0:4]
    context={
        "category" : category
    }
    return render(request,'index.html',context)

def single_course(request):
    return render(request,'single.html')

def contact_us(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
