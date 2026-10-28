
# from django.db import models
# from courses.models import Course


# class LearningMaterial(models.Model):
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.CASCADE,
#         related_name='materials'
#     )

#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     url = models.URLField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.title} - {self.course.title}"
