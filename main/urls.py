# main/urls.py

from django.urls import path
from .views import home, buy_album, finalize_order, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('buy/<int:album_id>/', buy_album, name='buy_album'),
    path('finalize/<int:album_id>/', finalize_order, name='finalize_order'),
    path('logout/', logout_view, name='logout'),
]
