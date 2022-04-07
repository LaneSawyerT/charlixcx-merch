from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_merch, name='merchandise'),
    path('<merch_id>', views.merchandise_info, name='merchandise_info'),
    path('add/', views.add_merchandise, name='add_merchandise'),
    path('edit/<int:merch_id>/', views.edit_merchandise,
         name='edit_merchandise'),
    path('delete/<int:merch_id>/', views.delete_merchandise,
         name='delete_merchandise'),
    ]
