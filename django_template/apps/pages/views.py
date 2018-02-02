from django.shortcuts import render
from django.template import RequestContext
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'pages/index.html'
