from django.urls import path
from . import views
urlpatterns = [
    path('search',views.search,name='search'),
    path('',views.home,name='home'),
    path('<slug:c_slug>/<slug:p_slug>/',views.prodetails,name='pro'),
    path('<slug:c_slug>',views.home,name='cat_prod'),

]