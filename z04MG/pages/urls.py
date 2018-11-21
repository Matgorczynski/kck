from django.urls import path

from .views import AboutPageView, HomePageView, DodatekPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('dodatek/', DodatekPageView.as_view(), name='dodatek'),
]
