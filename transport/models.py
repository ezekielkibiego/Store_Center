from django.db import models
from store.models import User
from django.core.validators import RegexValidator

class Transport(models.Model):
    PICKUP='Pick-Up'
    DELIVERY = 'Delivery'
    TRANSPORT_CHOICES=(
        (PICKUP,'Pick-Up'),
        (DELIVERY,'Delivery'),
        
    )
    transport_type = models.CharField(
        max_length=50,
        choices=TRANSPORT_CHOICES,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_owner')
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50,null=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phoneNumberRegex],max_length=10,verbose_name='Input your Phone Number ',help_text='Formart 0712345678')
    distance = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    goods = models.ForeignKey('units.Goods', on_delete=models.CASCADE, null=True, related_name='transport_goods')
    is_paid = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.transport_type

class AccessToken(models.Model):
    token = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'

    def __str__(self):
	    return self.token
