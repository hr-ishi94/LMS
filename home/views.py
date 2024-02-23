from django.shortcuts import render
from .models import Categories,Course,Level

def index(request):
    category = Categories.objects.all().order_by('id')[0:4]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    context={
        "category" : category,
        'course':course
    }
    return render(request,'index.html',context)

def single_course(request):
    category =Categories.get_all_categories(Categories)
    course_count= Course.objects.all().count()
    level= Level.objects.all()
    context = {
        "category" : category,
        'course_count':course_count,
        'level': level
    }
    return render(request,'single.html', context)

def contact_us(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
