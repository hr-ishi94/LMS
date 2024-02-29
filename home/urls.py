from django.urls import path,include
from . import views

app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('courses/',views.single_course,name='single_course'),
    path('product/filter-data',views.filter_data,name="filter-data"),
    path('contact/',views.contact_us,name='contact_us'),
    path('about_us/',views.about,name='about'),

    
]
