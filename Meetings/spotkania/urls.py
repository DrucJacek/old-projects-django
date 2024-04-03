from django.urls import path
from .views import spotkanie_detail, pedagog, uczen

urlpatterns = [
   path('test/<int:id>', spotkanie_detail, name='book_detail'),
   path('test2', pedagog, name="pedagog"),
   path('test3', uczen, name="uczen"),

]

