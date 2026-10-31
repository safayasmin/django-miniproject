from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['title','description']

    def clean_title(self):
        title=self.cleaned_data['title']

        if len(title)<2:
            raise forms.ValidationError(
                "Course title must contain at least 3 characters."
            )
        return title

    def clean_description(self):
        description=self.cleaned_data['description']

        if len(description)<10:
            raise forms.ValidationError(
                "Course description must contain at least 10 characters."
            )
        return description


