from django.contrib.admin.models import User
from shop.models import Category
import os
import django
from django.template.defaultfilters import slugify
from conf.choices import CATEGORY_CHOICES

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

# Models

# create categories
for category in CATEGORY_CHOICES:
    Category(name=category, slug=slugify(category)).save()

# create admin user
User.objects.create_superuser('admin@work.com', 'password')
