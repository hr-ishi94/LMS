from django.shortcuts import render
from .models import Categories,Course,Level

from django.template.loader import render_to_string
from django.http import JsonResponse


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
    course= Course.objects.all().order_by("id")
    level= Level.objects.all()
    context = {
        "category" : category,
        'course_count':course_count,
        'level': level,
        'course':course
    }
    return render(request,'single.html', context)
    
def filter_data(request):
    category = request.GET.getlist('category[]')
    if category:
        course= Course.objects.filter(category__id__in = category).order_by("-id")
    else:
        course= Course.objects.all().order_by("-id")

    

    t = render_to_string('ajax/course.html', {'course': course})

    return JsonResponse({'data': t})


def contact_us(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
