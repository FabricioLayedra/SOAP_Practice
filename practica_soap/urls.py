from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'daw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', views.mostrar_inidex,name='mostrar_inidex'),
    url(r'^formulario_getOilPrice/', views.mostrar_formulario_getOilPrice),
    url(r'^formulario_currentOilPrice/', views.mostrar_formulario_currentOilPrice),
    url(r'^getOilPrice/', views.getOilPrice),
    url(r'^currentOilPrice/', views.currentOilPrice),

]
