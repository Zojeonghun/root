from django.core import paginator
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render
from django.urls import reverse
from . import models, forms
from django.core.paginator import Paginator

def Knees(request):
    return render(request, 'knees/knees.html')


def search(request):

    form = forms.SearchForm(request.GET)

    if form.is_valid():
        activity = form.cleaned_data.get("activity")
        hope = form.cleaned_data.get("hope")
        age = form.cleaned_data.get("age")
        waterproof = form.cleaned_data.get("waterproof")
        
        filter_args = {}
        
        if activity is not None:
            filter_args["activity"] = activity

        # for a in activity:
        #     filter_args["activity"] = a
        # if activity is not None:
        #     filter_args["activity"] = activity
        
        if hope is not None:
            filter_args["hope"] = hope

        if age is not None:
            filter_args["age"] = age

        if waterproof is not None:
            filter_args["waterproof"] = waterproof


        knees = models.Feet.objects.filter(**filter_args)


    else:
        form = forms.SearchForm()
        return render(request, "knees/search.html", {"form": form})


    return render(request, "knees/knees_list.html", {"form": form, "knees": knees})