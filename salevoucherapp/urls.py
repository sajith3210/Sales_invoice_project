from . import views
from django.urls import path

urlpatterns = [
    path('', views.add_product,name='add_product'),
    path('bill_page', views.bill_page,name='bill_page'),
    path('edit_sale/<int:pk>/', views.edit_sale,name='edit_sale'),
    path('delete_sale/<int:pk>/', views.delete_sale,name='delete_sale'),
    path('show_product/', views.show_product,name='show_product'),
    # path('get_product/', views.get_product,name='get_product'),
    path('get_product_data/', views.get_product_data,name='get_product_data'),
    path('print_pdf/', views.print_pdf,name='print_pdf'),
    
]
