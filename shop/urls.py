from django.urls import path
from shop.views import (
    product_list,
    product_detail,
    product_revisit,
    service_page,
    support_page,
    service_purchased,
    landing_page
)

app_name = 'shop'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('purchased/', product_list, name='product_list'),
    path('<int:id>/<slug:slug>/', product_detail,
         name='product_detail'),
    path('<slug:category_slug>/', product_list,
         name='product_list_by_category'),
    path('revisit/<int:id>/<slug:slug>/', product_revisit,
         name='product_revisit'),
    path('services', service_page, name='service_page'),
    path('supports', support_page, name='support_page'),
    path('service/purchased/', service_purchased, name='service_purchased'),

]
