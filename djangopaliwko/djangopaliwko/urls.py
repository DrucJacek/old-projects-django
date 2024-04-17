from django.contrib import admin
from django.urls import path, include
from paliwoapp.views import welcome


urlpatterns = [
    path('', welcome, name='welcome'),
    path('paliwkoapp/', include("paliwoapp.urls")),
    path('admin/', admin.site.urls),

]
