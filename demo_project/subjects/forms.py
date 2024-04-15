from django import forms
from .models import Subjects,Lectures

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = "__all__"


class LecturesForm(forms.ModelForm):
    class Meta:
        model= Lectures
        fields= "__all__"

        
