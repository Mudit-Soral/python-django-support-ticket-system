from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ticket_list, name = 'ticket_list'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('edit/<int:id>/', views.edit_ticket, name = 'edit_ticket'),
    path('delete/<int:id>/', views.delete_ticket, name = 'delete_ticket'), 
    path('ticket/<int:id>/', views.detail_ticket, name= 'details_ticket'),
    path('login/', auth_views.LoginView.as_view(template_name = 'tickets/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name ='logout')
]

