from django.shortcuts import render
from django.urls import reverse_lazy
from . models import Lectures,Subjects
from . forms import SubjectsForm,LecturesForm
from django.views.generic import ListView, DeleteView,DetailView,UpdateView,CreateView


class CreateSubject(CreateView):
    model = Subjects
    template_name = "Subject/subject_edit.html"
    form_class = SubjectsForm
    success_url = reverse_lazy("subject_list")

class UpdateSubject(UpdateView):
    model = Subjects
    template_name= "Subject/subject_edit.html"
    form_class = SubjectsForm
    success_url = reverse_lazy("subject_list")

class DeleteSubject(DeleteView):
    model=Subjects
    template_name= "subject/subject_delete.html"
    success_url = reverse_lazy("subject_list")

class SubjectList(ListView):
    model = Subjects
    template_name = "Subject/subject_list.html"
    context_object_name = "subjects"

class SubjectDetail(DetailView):
    model= Subjects
    template_name = "subject/subject_detail.html"



class CreateLecture(CreateView):
    model = Lectures
    template_name = "lecture/lecture_edit.html"
    form_class = LecturesForm
    success_url = reverse_lazy("lecture_list")

class UpdateLecture(UpdateView):
    model = Lectures
    template_name= "lecture/lecture_edit.html"
    form_class = LecturesForm
    success_url = reverse_lazy("lecture_list")

class DeleteLecture(DeleteView):
    model=Lectures
    template_name= "lecture/lecture_delete.html"
    success_url = reverse_lazy("lecture_list")

class LectureList(ListView):
    model = Lectures
    template_name = "lecture/lecture_list.html"
    context_object_name = "lectures"

class LectureDetail(DetailView):
    model= Lectures
    template_name = "lecture/lecture_detail.html"






