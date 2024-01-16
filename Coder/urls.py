from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("podologo/list", views.podologo_list, name="podologo_list"),
    path("podologo/form", views.podologo_form, name="podologo_form"),
]
