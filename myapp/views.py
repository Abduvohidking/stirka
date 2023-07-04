from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPage(TemplateView):
     template_name = "about.html"
