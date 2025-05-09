from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_to_basket, name='add_to_basket'),
    path('my/', views.view_my_basket, name='view_my_basket'),
    path('history/', views.my_purchase_history, name='my_purchase_history'),

    path('all/', views.view_all_baskets, name='view_all_baskets'),
    path('update/<int:pk>/<str:action>/', views.update_basket_status, name='update_basket_status'),
]