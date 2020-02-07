from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='shopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='TrackerStatus'),
    path('search/',views.search,name='Search'),
    path('product/<int:myid>',views.product,name='Product'),
    path('checkout/',views.checkout,name='checkout')
]