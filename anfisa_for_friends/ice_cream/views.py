from django.shortcuts import get_object_or_404, render

from ice_cream.models import IceCream

def ice_cream_detail(request, pk):
    template_name = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.values(
            'title', 'description'
        ).filter(is_published=True),
        pk=pk
    )

    # ice_cream = get_object_or_404(
    #    # Первый аргумент - QuerySet:
    #    IceCream.objects.values('title', 'description'),
    #    # Второй аргумент - условие, по которому фильтруются записи из QuerySet:
    #    pk=pk)
    # Вызываем .get() и в его параметрах указываем условия фильтрации:
    # ice_cream = get_object_or_404(IceCream, pk=pk)
    # ice_cream = IceCream.objects.get(pk=pk)
    # ice_cream = IceCream.objects.get(title__contains='мороженое')
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template_name, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {}
    return render(request, template, context)
