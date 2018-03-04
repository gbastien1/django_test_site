from django.shortcuts import render
from django.views import generic

from .models import Category, Product



class CatalogIndexView(generic.ListView):
	model = Category
	template_name = 'pages/catalog_index.html'


class CatalogCategoryView(generic.ListView):
	model = Product
	# TODO filter products by category using param slug
	template_name = 'pages/catalog_category_detail.html'
	
	def get_queryset(self):
		slug = self.kwargs['slug']
		queryset = Product.objects.filter(category__slug=slug) # use double underscores to get attributes of foreign key object
		return queryset
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['url_slug'] = self.kwargs['slug']
		return context


class CatalogProductView(generic.DetailView):
	model = Product
	template_name = 'pages/catalog_product_detail.html'