from django.urls import path
from .views import (CreateSubject,DeleteSubject,SubjectDetail,UpdateSubject,SubjectList,
                    CreateLecture,DeleteLecture,UpdateLecture,LectureDetail,LectureList)

urlpatterns = [
    path("subject/new",CreateSubject.as_view(),name="new subject"),
    path("subject/<int:pk>/detail",SubjectDetail.as_view(),name="subject_detail"),
    path("subject/list",SubjectList.as_view(),name="subject_list"),
    path("subject/<int:pk>/edit",UpdateSubject.as_view(),name="update subject"),
    path("subject/<int:pk>/delete",DeleteSubject.as_view(),name="delete subject"),
    path("lecture/new",CreateLecture.as_view(),name="new lecture"),
    path("lecture/<int:pk>/detail",LectureDetail.as_view(),name="lecture_detail"),
    path("lecture/list",LectureList.as_view(),name="lecture_list"),
    path("lecture/<int:pk>/delete",DeleteLecture.as_view(),name ='delete lecture'),
    path("lecture/<int:pk>/edit",UpdateLecture.as_view(),name="update subject")
]