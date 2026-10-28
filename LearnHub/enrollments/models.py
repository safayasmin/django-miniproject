from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from courses.models import Course

class Enrollment(models.Model):
    student=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='student_enrollments'
    )

    enrolled_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['student','course'],
                name='unique_student_course_enrollment'
            )
        ]
    def __str__(self):
        return f"{self.student.username}-{self.course.title}"
            