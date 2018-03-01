from django.shortcuts import render
from django.views import generic

from .models import Category, Product

# Create your views here.

class CatalogIndexView(generic.ListView):
	model = Category
	template_name = 'pages/catalog_index.html'


class CatalogCategoryView(generic.ListView):
	model = Product
	# TODO filter products by category using param slug
	template_name = 'pages/catalog_category_detail.html'
	
	def get_queryset(self):
		slug = self.kwargs['slug']
		queryset = Product.objects.filter(category__slug=slug)
		return queryset