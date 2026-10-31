from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Course(models.Model):
    students = models.ManyToManyField(
    User,
    through='enrollments.Enrollment',
    related_name='enrolled_courses',
    blank=True
    )

  
    title=models.CharField(max_length=200)
    description=models.TextField()
    instructor=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses'  
    )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        permissions=[
            ("can_publish_course","can publish course"),
            ("can_manage_enrollments","can manage enrollments"),
        ]