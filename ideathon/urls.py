from django.contrib import admin
from django.urls import path, include
import board.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
]
