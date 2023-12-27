from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def single_course(request):
    return render(request,'single.html')

def contact_us(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
