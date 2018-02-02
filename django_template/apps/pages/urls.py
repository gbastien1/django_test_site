from django.urls import path

from . import views


app_name = 'pages'
urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name="index"),
    path('about/', views.IndexView.as_view(), name="about"),
    path('contact/', views.IndexView.as_view(), name="contact"),
]