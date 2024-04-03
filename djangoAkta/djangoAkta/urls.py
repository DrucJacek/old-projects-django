
from django.contrib import admin
from django.urls import path, include
from files.views import home

urlpatterns = [
    path('', home, name='home'),
    path('files/', include("files.urls")),
    path('admin/', admin.site.urls),

]
