# Script to setup a demo recommending system

from shop.models import Product
from shop.recommender import Recommender

r = Recommender()

dell_inspiron = Product.objects.get(name='Dell Inspiron')
dell_laptop = Product.objects.get(name='Dell Laptop')
dell_monitor = Product.objects.get(name='Dell Monitor')
dell_keyboard = Product.objects.get(name='Dell Keyboard')


r.products_bought([dell_monitor, dell_keyboard])
r.products_bought([dell_inspiron, dell_laptop])
r.products_bought([dell_inspiron, dell_keyboard, dell_monitor])

