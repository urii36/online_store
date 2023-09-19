from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import home_page, contacts, product_detail

app_name = 'catalog'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('contacts/', contacts, name='contacts'),
    path('product/<pk>/', product_detail, name='product_detail'),
]
