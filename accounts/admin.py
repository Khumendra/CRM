CREDIENTIALS = [{
    'username': 'django',
    'password': 'djangoAdmin',
    'email': 'django@gmail.com'
}, {
    'username': 'django2',
    'password': 'pwddjangoAdmin2',
    'email': 'django2@gmail.com'
},
]

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
