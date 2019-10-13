from django.urls import path
from payment.views import after_payment

app_name = 'payment'

urlpatterns = [
    path('after_payment/', after_payment, name='after_payment'),
]