# main/admin.py

from django.contrib import admin
from .models import Album, Sale

admin.site.register(Album)
admin.site.register(Sale)
