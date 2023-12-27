from django.urls import path,include
from . import views

app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('single/course/',views.single_course,name='single_course'),
    path('contact/',views.contact_us,name='contact_us'),
    path('about_us/',views.about,name='about'),

    
]
