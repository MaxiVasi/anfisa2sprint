from django.contrib import admin

# Register your models here.

# Из модуля models импортируем модель Category...
from .models import Category, IceCream, Topping, Wrapper

# ...и регистрируем её в админке:
#admin.site.register(Category)
#admin.site.register(IceCream)

admin.site.empty_value_display = 'Не задано'

class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

# Регистрируем класс с настройками админки для моделей IceCream и Category:
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
# Регистрируем модели Topping и Wrapper,
# чтобы ими можно было управлять через админку
# (интерфейс админки для этих моделей останется стандартным):

admin.site.register(Topping)
admin.site.register(Wrapper)
