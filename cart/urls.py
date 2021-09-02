from django.urls import path
from . import views
urlpatterns = [
    path('cart',views.cart,name='cart'),
    path('add/<int:product_id>/',views.add_cart,name='add'),
    path('min/<int:product_id>/',views.mincart,name='min'),
    path('delete/<int:product_id>/',views.delete,name='delete')
]