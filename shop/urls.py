from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path(
        '',
        views.landing_page,
        name='landing_page',
    ),
    path(
        'search/',
        views.search_page,
        name='search_page',
    ),
    path(
        'purchased/',
        views.product_list,
        name='product_list',
    ),
    path(
        '<int:id>/<slug:slug>/',
        views.product_detail,
        name='product_detail',
    ),
    path(
        '<slug:category_slug>/',
        views.product_list,
        name='product_list_by_category',
    ),
    path(
        'revisit/<int:id>/<slug:slug>/',
        views.product_revisit,
        name='product_revisit',
    ),
    path(
        'services',
        views.service_page,
        name='service_page',
    ),
    path(
        'supports',
        views.support_page,
        name='support_page',
    ),
    path(
        'service/purchased/',
        views.service_purchased,
        name='service_purchased',
    ),
    path(
        'api/products/',
        views.ProductListCreateAPIView.as_view(),
    ),
]