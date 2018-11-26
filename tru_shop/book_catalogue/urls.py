from django.conf.urls import url
from book_catalogue.views import view

app_name = 'book_catalogue'

urlpatterns = [
    # url(r'^create/', create, name='create'),
    # view/<int:pizza_order_id>
    url(r'^view/book_catalogue', view, name='view'),
    # url(r'^close/(?P<pizza_order_id>[0-9]+)/', close, name='close'),

    # url(r'^stats/', stats, name='stats'),
]