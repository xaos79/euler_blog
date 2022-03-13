from django.shortcuts import render
from .models import Action
from django.views import generic


class HomeList(generic.ListView):
    model = Action
    template_name = 'action/home.html'
    context_object_name = 'actions'


class SolutionDetailView(generic.DetailView):
    model = Action
    template_name = 'action/detail.html'
    context_object_name = 'action'
