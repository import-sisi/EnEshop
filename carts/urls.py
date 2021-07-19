from django.urls import path
from .views import (
    cart_update, 
    cart_home,
    checkout_home,
    checkout_done_view,
)

urlpatterns = [
    path('', cart_home, name='home'),
    path('checkout/success/', checkout_done_view, name='success'),
    path('checkout/', checkout_home, name='checkout_home'),
    path('update/', cart_update, name='update'),
]

