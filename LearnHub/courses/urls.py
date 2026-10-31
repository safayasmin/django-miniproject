from django.urls import path
from . import views

urlpatterns=[
    path('',views.course_list,name='course_list'),
    path('publish/',views.publish_course,name='publish_course'),
    path('manage/<int:course_id>/',views.manage_course,name='manage_course'),
    path('create/',views.create_course,name='create_course'),
]