from django.shortcuts import redirect, render
from . import models
from . import forms

def index(request):
    return render(request, "Coder/index.html")


def podologo_list(request):
    consulta = models.Podologo.objects.all()
    contexto = {"podologas": consulta}
    return render(request, "Coder/podologo_list.html", contexto)


def podologo_form(request):
    if request.method == "POST":
        form = forms.PodolodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("podologo_list")
    else:
        form = forms.PodolodoForm()
    return render(request, "Coder/podologo_form.html", {"form": form})