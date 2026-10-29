from django.urls import path
from . import views

urlpatterns=[
    path('',views.course_list,name='course_list'),
    path('publish/',views.publish_course,name='publish_course'),
]