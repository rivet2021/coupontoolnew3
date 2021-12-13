from django.contrib import admin
from .models import copons,profile,Payment_details, Payment_details_customer,Subscription_details

# Register your models here.
admin.site.register(copons)
admin.site.register(profile)
admin.site.register(Payment_details)
admin.site.register(Payment_details_customer)
admin.site.register(Subscription_details)

