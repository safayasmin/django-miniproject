# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def course_list(request):
#     return HttpResponse("Welcome to learnhub courses!")


from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Course
from django.contrib import messages

from .forms import CourseForm
from django.contrib.auth.decorators import permission_required
from django.db import transaction

# get_object_or_404() database-il course undo ennu check cheyyum. Course illenkil 404 error return cheyyum.
from django.shortcuts import get_object_or_404

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

# Ithu vere instructor-ude course manage cheyyunnath prevent cheyyanulla additional ownership check aanu.



@login_required
def manage_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.user.is_superuser or request.user.groups.filter(name='Admin').exists():
        return HttpResponse(f"Admin can manage: {course.title}")

    if course.instructor != request.user:
        return HttpResponse("You cannot manage another instructor's course.")

    if not request.user.has_perm('courses.change_course'):
        return HttpResponse("You don't have permission to change courses.")

    return HttpResponse(f"You can manage: {course.title}")


# ----------------------------
# Browser-il ee address type cheyyuka:

# http://127.0.0.1:8000/admin/
# Step 2: Course open cheyyuka
# 1. Login cheyyuka.
# 2. Courses section-il Courses click cheyyuka.
# 3. Course list-il ninte course name click cheyyuka.
# Step 3: URL nokkuka
# Course open cheythal browser-inte mukalil address bar-il ingane oru URL kaanum:

# http://127.0.0.1:8000/courses/manage/2/
# http://127.0.0.1:8000/admin/courses/course/1/change/

# ---------------------------------



@login_required
@permission_required('courses.add_course',raise_exception=True)
def create_course(request):
    if request.method=='POST':
        form=CourseForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                course=form.save(commit=False)
                course.instructor=request.user
                course.save()      

            messages.success(request,"Course Created Successfully ")
            return redirect('course_list')
    else:
        form=CourseForm()

    return render(request,'courses/create_course.html',{'form':form})

        
