from django.db import models

# Create your models here.


class Base(models.Model):
    created = models.DateField('Create', auto_now_add=True)  # When the object will create, the date automatically will be created (auto_now_add, only when add an object)
    modified = models.DateField('Update', auto_now=True)  # When the object will modified, the date automatically will be created (auto_now only that when an object was modified)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


# Created to modeling our services
# When we register a new service, we can inform to the type of service that the new register has
class Feature(Base):
    ICON_CHOICES = (  # Tuple of tuples for transforming on 'combo box' when we register an icon
        ('lni-vector', 'Vector'),
        ('lni-pallet', 'Pallet'),
        ('lni-stats-up', 'Graphic'),
        ('lni-code-alt', 'Code'),
        ('lni-lock', 'Lock'),
        ('lni-code', 'HTML'),
    )
    service = models.CharField('Service', max_length=100)
    description = models.TextField('Description', max_length=500)
    icon = models.CharField('Icon', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'
    
    def __str__(self):
        return self.service


class Pricing(Base):
    # When we register a new pricing of service, we can inform to the value and type of service that the new register has
    title = models.CharField('Title', max_length=100)
    service = models.ForeignKey('core.Feature', verbose_name='Service', on_delete=models.CASCADE)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    description = models.TextField('Description', max_length=500)
    link = models.CharField('Link', max_length=100, default='#')

    class Meta:
        verbose_name = 'Pricing'
    
    def __str__(self):
        return self.title

