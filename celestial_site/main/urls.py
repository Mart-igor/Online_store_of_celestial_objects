from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home_page'),
    path('shop', views.celestial_list, name='celestial_list'),
    path('shop/category/<slug:category_slug>/', views.celestial_list, name='celestial_list'),
    path('shop/<slug:celestial_slug>/', views.detail, name='detail'),
]
