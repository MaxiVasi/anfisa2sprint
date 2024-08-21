from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings

urlpatterns = [
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('ice_cream/', include('ice_cream.urls')),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()

#if settings.DEBUG:
#    import debug_toolbar
#    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
#    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

#if not settings.TESTING:
#    urlpatterns = [
#        *urlpatterns,
#    ] + debug_toolbar_urls()