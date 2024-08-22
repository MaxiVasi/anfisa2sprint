from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import Category, IceCream


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )



    # ice_cream_list = IceCream.objects.values('id', 'title', 'category__title')
    # ice_cream_list = IceCream.objects.select_related('category')
    # ice_cream_list = IceCream.objects.select_related('wrapper').filter(
    #    is_on_main=True, is_published=True).order_by('title')
        
    
    # Запрос:
    # ice_cream_list = IceCream.objects.all()
    # ice_cream_list = IceCream.objects.values('id', 'title')
    # ice_cream_list = IceCream.objects.values(
    #       'id', 'title', 'description'
    #    ).filter(
    #    (Q(is_on_main=True) & Q(is_published=True))
    #    | (Q(title__contains='пломбир') & Q(is_published=True))
    #).order_by('title')[1:4]

    # categories = Category.objects.values(
    #    'id', 'output_order', 'title'
    # ).order_by(
    #    # Сортируем записи по значению поля output_order,
    #    # а если значения output_order у каких-то записей равны -
    #    # сортируем эти записи по названию в алфавитном порядке.
    #    'output_order', 'title'
    # )

    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
        # 'categories': categories
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
