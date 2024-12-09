from django.shortcuts import render, get_object_or_404
from .models import Celestial, Category
from django.core.paginator import Paginator
from cart.forms import CartAddCelestialForm


def index(request):
    celestial_objs = Celestial.objects.filter(available=True)
    return render(request, 'main/index.html', context={'celestial_objs': celestial_objs})

def detail(request, celestial_slug):
    celestial_obj = get_object_or_404(Celestial, slug=celestial_slug)
    cart_celestial_form = CartAddCelestialForm()
    return render(request, 'main/detail.html', context={'celestial_obj': celestial_obj,
                                                        'cart_celestial_form': cart_celestial_form})

def celestial_list(request, category_slug=None):
    category = None
    category_slug = category_slug
    celestial_objs = Celestial.objects.filter(available=True)
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        celestial_objs = category.celestial.filter(available=True)
    paginator = Paginator(celestial_objs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/celestial_list.html', context={'celestial_objs': page_obj,
                                                                'category': category,
                                                                'categories': categories,
                                                                'category_slug': category_slug,
                                                                'page_obj': page_obj})
