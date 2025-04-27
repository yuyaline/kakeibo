from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('add/', views.add_expense, name='add_expense'),
    path('day/<int:year>/<int:month>/<int:day>/', views.day_detail, name='day_detail'),  
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),  
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),  
]
