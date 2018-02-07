from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
	path('', views.CatalogIndexView.as_view(), name="index"),
]
