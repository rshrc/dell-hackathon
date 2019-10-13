from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('search/', views.search_page, name='search_page'),
    path('purchased/', views.product_list, name='product_list'),
    path('analytics/<int:product_id>', views.analytics, name='analytics'),
    path('<int:id>/<slug:slug>/', views.product_detail_page,
         name='product_detail_page'),
    path('<slug:category_slug>/', views.category_list_page,
         name='category_list_page'),
    path('revisit/<int:id>/<slug:slug>/`',
         views.product_revisit, name='product_revisit'),
    path('services', views.service_page, name='service_page'),
    path('supports', views.support_page, name='support_page'),
    path('service/purchased/', views.service_purchased, name='service_purchased'),
    path('api/products/', views.ProductListCreateAPIView.as_view()),
    path('api/reviews/<int:pk>', views.ReviewDataAPI.as_view()),
]
