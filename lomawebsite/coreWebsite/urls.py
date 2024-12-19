# my_app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('concessions/', views.ConcessionsView.as_view(), name='concessions'),
    path('ticket-prices/', views.TicketPricesView.as_view(), name='ticket_prices'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
