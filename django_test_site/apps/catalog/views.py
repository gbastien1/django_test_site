from django.shortcuts import render
from django.views import generic

# Create your views here.

class CatalogIndexView(generic.TemplateView):
	template_name = 'pages/catalog_index.html'
