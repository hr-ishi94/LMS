from django.shortcuts import render
from .models import Categories,Course

def index(request):
    category= Categories.objects.all().order_by('id')[0:4]
    course=Course.objects.filter(status = 'PUBLISH').order_by('-id')
    context={
        "category" : category,
        'course':course
    }
    return render(request,'index.html',context)

def single_course(request):
    return render(request,'single.html')

def contact_us(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
