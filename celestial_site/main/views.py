from django.shortcuts import render, get_object_or_404
from .models import Celestial, Category


def index(request):
    celestial_objs = Celestial.objects.filter(available=True)
    return render(request, 'main/index.html', context={'celestial_objs': celestial_objs})

def detail(request, celestial_slug):
    celestial_obj = get_object_or_404(Celestial, slug=celestial_slug)
    return render(request, 'main/detail.html', context={'celestial_obj': celestial_obj})

def celestial_list(request, category_slug=None):
    category = None
    category_slug = category_slug
    celestial_objs = Celestial.objects.filter(available=True)
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        celestial_objs = category.celestial.filter(available=True)
    return render(request, 'main/celestial_list.html', context={'celestial_objs': celestial_objs,
                                                                'category': category,
                                                                'categories': categories,
                                                                'category_slug': category_slug})
