
from django.contrib import admin
from django.urls import path, include
from spotkania.views import home, spotkanie_detail, pedagog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('spotkanie/', include('spotkania.urls')),

]
