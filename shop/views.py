from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category, Product, Service, Support, Review
from cart.forms import CartAddProductForm
from shop.recommender import Recommender
from rest_framework import generics, filters
from shop.serializers import ProductSerializer, ReviewSerializier
from conf import fields
from django.http import HttpResponse
from markdown import markdown
from requests import get
from json import loads

class ProductListCreateAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = list(fields.PRODUCT_FIELDS_API)


# query to get reviews
# Review.objects.filter(product__name=product_name)

class ReviewDataAPI(generics.ListAPIView):
    # queryset = Review.objects.filter(product__name=product_name)
    serializer_class = ReviewSerializier

    def get_queryset(self):
        product_id = self.kwargs['pk']
        queryset = Review.objects.filter(product_id=product_id)
        return queryset


def landing_page(request):

    products = Product.objects
    # count of products in each category
    categories = dict()
    for category in Category.objects.all():
        categories[str(category)] = [
            category.slug,
            products.filter(category__name__exact=category).count(),
        ]

    return render(
        request, 'product/landing_page.html', {
            'categories': categories.items(),
            'products': products.all(),
            # 'current_user': current_user,
            'location': "Jaipur, Rajasthan"
        })


def product_detail_page(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_add_product_form = CartAddProductForm()
    reviews = Review.objects.select_related().filter(product=product)

    return render(
        request, 'product/product_detail_page.html', {
            'product': product,
            'description': markdown(product.description),
            'cart_add_product_form': cart_add_product_form,
            'reviews': reviews
        })


def product_list(request, category_slug=None):
    print("hello world")
    category = None
    categories = Category.objects.all()
    current_user = request.user.userprofile
    products = request.user.userprofile.product_list.all()
    print("Products of current User : " + str(products))
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'current_user': current_user})


def category_list_page(request, category_slug):
    current_user = request.user.userprofile
    products = Product.objects

    # count of products in each category
    categories = dict()
    for category in Category.objects.all():
        categories[str(category)] = [
            category.slug,
            products.filter(category__name__exact=category).count(),
        ]

    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category__name__exact=category)

    return render(
        request, 'product/category_list_page.html', {
            'category': category,
            'categories': categories.items(),
            'products': products.all(),
            'current_user': current_user,
            'location': "Jaipur, Rajasthan"
        })


def product_revisit(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(
        request, 'product/revisit.html', {
            'product': product,
            'cart_product_form': cart_product_form,
            'recommended_products': recommended_products
        })


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)

    cart_product_form = CartAddProductForm()
    return render(request, 'product/service_detail.html', {
        'service': service,
        'cart_product_form': cart_product_form
    })


def service_page(request):
    services = Service.objects.all()

    return render(request, 'product/services.html', {'services': services})


def service_purchased(request):
    current_user = request.user.userprofile
    print("Current User : " + str(current_user.conversion_rate))

    if current_user.conversion_rate == 0:
        current_user.conversion_rate = 1
        request.user.userprofile.save()
    print("Current User : " + str(current_user.conversion_rate))
    return render(request, 'product/service_purchased.html', {})


def support_page(request):
    supports = Support.objects.all()

    return render(request, 'product/support.html', {'supports': supports})


def search_page(request):
    # print('hello')
    
    response = loads(get(f'http://localhost:8000/api/products?search={request.GET["search_input"]}').text)
    for product in response:
        product["url"] = f'/{product["id"]}/{product["slug"]}'
        print(product["url"])
    
    # print(request.GET["search_input"])
    # return render(request, 'product/search.html', {})
    return HttpResponse('Search')


def analytics(request, product_id):
    return render(request, 'analytics/index.html', {'product_id': product_id})
