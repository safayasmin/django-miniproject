# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def course_list(request):
#     return HttpResponse("Welcome to learnhub courses!")



from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Course

from django.contrib.auth.decorators import permission_required


# Ithu login cheytha user-in courses list kaanikkunnu.
# Admin: ella courses-um kaanum.
# Instructor: swantham courses mathram kaanum.
# Student: ippol ella courses-um browse cheyyam.

@login_required
def course_list(request):
    user = request.user

    if user.is_superuser or user.groups.filter(name='Admin').exists():
        courses = Course.objects.all()
        role = "Admin"

    elif user.groups.filter(name='Instructor').exists():
        courses = Course.objects.filter(instructor=user)
        role = "Instructor"

    elif user.groups.filter(name='Student').exists():
        courses = Course.objects.all()
        role = "Student"

    else:
        return HttpResponse("You don't have permission to access courses.")

    course_names = [course.title for course in courses]

    return HttpResponse(
        f"Welcome {role}! Courses: {', '.join(course_names) if course_names else 'No courses available.'}"
    )



@permission_required('courses.can_publish_course')
def publish_course(request):
    return HttpResponse('you have a permission to publish a course !')