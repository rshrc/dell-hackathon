from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from conf.choices import CATEGORY_CHOICES


class Category(models.Model):
    '''
    Details about the category of a product
    '''
    name = models.CharField(
        max_length=200,
        db_index=True,
        choices=CATEGORY_CHOICES,
        help_text="Enter category name of product",
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_list_page', args=[self.slug])


class Product(models.Model):
    '''
    Details about the product
    '''
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=200,
        db_index=True,
    )
    slug = models.SlugField(
        max_length=200,
        db_index=True,
    )
    small_image = models.ImageField(
        upload_to='products/small/%Y/%m/%d', blank=True)
    large_image = models.ImageField(
        upload_to='products/large/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    conversion_rate = models.IntegerField(default=0)

    class Meta:
        ordering = (
            'name',
            'category',
            'price',
        )
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    # when revisiting the website
    def get_absolute_url(self):
        return reverse('shop:product_revisit', args=[self.id, self.slug])

    # when visiting the site for the first time
    def get_absolute_url_visit_1(self):
        return reverse('shop:product_detail_page', args=[self.id, self.slug])


class Service(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, default="")
    description = models.TextField(blank=True)
    conversion_rate = models.IntegerField(default=0, blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:service_page', args=[self.id, self.slug])


class Support(models.Model):
    name = models.CharField(max_length=400, db_index=True)
    slug = models.SlugField(max_length=400, db_index=True, default="")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:support_page', args=[self.id, self.slug])


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    stars = models.IntegerField(default=0, blank=True, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])

    def __str__(self):
        return self.review
