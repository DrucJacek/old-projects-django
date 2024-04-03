
from django.contrib import admin
from django.urls import path, include
from website.views import welcome, detail, rooms_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),
    path('website/', include('website.urls')),
]
