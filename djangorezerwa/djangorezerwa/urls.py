
from django.contrib import admin
from django.urls import path, include
from pokojeapp.views import welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('pokojeapp/', include("pokojeapp.urls")),
    path('admin/', admin.site.urls),
]
