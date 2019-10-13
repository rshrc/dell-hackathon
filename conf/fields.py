PRODUCT_FIELDS = (
    'id',
    'category',
    'name',
    'slug',
    'small_image',
    'large_image',
    'description',
    'price',
    'available',
    'created',
    'updated',
    'conversion_rate',
)

PRODUCT_FIELDS_API = (
    'category__name',
    'name',
)

USER_PROFILE_FIELDS = (
    'birthday',
    'city',
    'country',
    'gender',
    'occupation',
)

REVIEW_FIELDS = (
    'user',
    'product',
    'review',
    'stars',
)
