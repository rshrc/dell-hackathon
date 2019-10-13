from django.shortcuts import render


def after_payment(request):
    return render(request, 'payment/after_payment.html', {})
