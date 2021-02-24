from django.contrib import admin
from .models import Feature, Pricing

# Register your models here.


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('service', 'active', 'modified')


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'modified')

