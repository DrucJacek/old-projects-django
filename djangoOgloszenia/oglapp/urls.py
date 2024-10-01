from django.urls import path


from . import views


urlpatterns = [
    path('detail/<int:id>', views.tresc, name='tresc' ),
    path('uzytkownik', views.uzytkownik, name='uzytkownik'),
    path('ksiazka', views.ksiazka, name='ksiazka'),
    path('new', views.new, name='new'),
    path('add', views.add, name='add'),
]