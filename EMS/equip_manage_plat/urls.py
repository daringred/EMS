from django.conf.urls import url
from . import views
app_name = 'equip_manage_plat'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    # url(r'^imei/', views.search_imei, name='imei'),
    # url(r'^code/', views.search_code, name='code'),
    # url(r'^borrower/', views.search_borrower, name='borrower'),

]
