from django.urls import path

from lectures import views

urlpatterns = [
    # path("", views.data),
    # path("json-data/", views.json_data),
    path("lectures/", views.lectures_list),
    path("instructors/", views.instructors_list),
    path("students/", views.students_list),
    path("tests/", views.tests_list),

    # path("tests/", views.tests_list),
 
]