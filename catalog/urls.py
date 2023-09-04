from django.urls import path

from catalog.views import home_page, contacts

app_name = 'catalog'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('contacts/', contacts, name='contacts'),
]