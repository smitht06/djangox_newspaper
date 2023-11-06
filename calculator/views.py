from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class CalcView(TemplateView):
    template_name = "calculator/calculator.html"