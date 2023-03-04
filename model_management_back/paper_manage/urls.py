from django.urls import path

from . import views

app_name = 'paper_manage'

urlpatterns = [
    path('search', views.search_paper, name='search'),
]