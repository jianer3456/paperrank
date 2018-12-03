from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Author, Paper, PaperAuthor

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'homepage/index.html'
