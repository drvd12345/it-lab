
# studentData/forms.py
from django import forms

# Static list of subjects
SUBJECT_CHOICES = [('Math', 'Math'), ('Science', 'Science'), ('History', 'History')]

class StudentDataForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    roll = forms.CharField(label='Roll', max_length=100)
    subjects = forms.ChoiceField(label='Subjects', choices=SUBJECT_CHOICES)
