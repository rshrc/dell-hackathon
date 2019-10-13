import os
import django
from django.template.defaultfilters import slugify
from conf.choices import CATEGORY_CHOICES, PRODUCT_CHOICES
from datetime import date
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'conf', 'img')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

# Models
from shop.models import Category, Product
from users.models import User

# create categories
for category in CATEGORY_CHOICES:
    Category(name=category, slug=slugify(category)).save()

# create admin user
User.objects.create_superuser('admin@work.com', 'password')

today = date.today()
# create media dir
os.mkdir(MEDIA_DIR)
# create products
os.mkdir(os.path.join(MEDIA_DIR, 'products'))
# create small images dir
os.mkdir(os.path.join(MEDIA_DIR, 'products', 'small'))
os.mkdir(os.path.join(MEDIA_DIR, 'products', 'small', str(today.year)))
os.mkdir(os.path.join(MEDIA_DIR, 'products', 'small', str(today.year), str(today.month)))
os.mkdir(os.path.join(MEDIA_DIR, 'products', 'small', str(today.year), str(today.month), str(today.day)))

# create large images dir
os.mkdir(os.path.join(MEDIA_DIR, 'products', 'large'))
os.mkdir(os.path.join(MEDIA_DIR, 'products', 'large', str(today.year)))
os.mkdir(os.path.join(MEDIA_DIR, 'products', 'large', str(today.year), str(today.month)))
os.mkdir(os.path.join(MEDIA_DIR, 'products', 'large', str(today.year), str(today.month), str(today.day)))

# create products
for product in PRODUCT_CHOICES:
    # for small image
    path = shutil.copy(os.path.join(IMG_DIR, product['small_image']), os.path.join(MEDIA_DIR, 'products', 'small', str(today.year), str(today.month), str(today.day)))
    small_image_path = f'{os.sep}'.join(path.split(os.sep)[7:])
    # for large image
    path = shutil.copy(os.path.join(IMG_DIR, product['large_image']), os.path.join(MEDIA_DIR, 'products', 'large', str(today.year), str(today.month), str(today.day)))
    large_image_path = f'{os.sep}'.join(path.split(os.sep)[7:])
    Product(category=Category.objects.get(name=product['category']), name=product['name'], slug=slugify(
        product['name']), small_image=small_image_path, large_image=large_image_path, description=product['description'], price=product['price'],).save()
