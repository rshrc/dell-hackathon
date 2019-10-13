from shop.models import Category, Product
from users.models import User
import os
import django
from django.template.defaultfilters import slugify
from conf.choices import CATEGORY_CHOICES, PRODUCT_CHOICES

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

# Models

# create categories
for category in CATEGORY_CHOICES:
    Category(name=category, slug=slugify(category)).save()

# create admin user
User.objects.create_superuser('admin@work.com', 'password')

# create products
for product in PRODUCT_CHOICES:
    Product(product['category'], product['name'], slugify(
        product['name']), product['small_image'], product['large_image'], product['description'], product['price'], product['available'], product['small_image']).save()
