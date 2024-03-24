from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

CONDITIONS = [
        # Furniture
        ("GOOD", "Good"),
        ("SDMG", "Slightly damaged"),
        ("BRKN", "Broken"),
        # Electronics
        ("WRKN", "Working"),
        ("PWRK", "Partially working"),
        ("NWRK", "Not working")
]

CATEGORIES = [
        ("ELC", "Electronics"),
        ("FUR", "Furniture")
]

USER_ROLES= [
        ("ADT", "Auditor"),
        ("CDN", "Custodian"),
        ("HOD", "Head of Department")
]

class User(AbstractUser):
    role = models.CharField(max_length=24, choices=USER_ROLES)

    def __str__(self):
        return self.username

class StockCondition(models.Model):
    condition = models.CharField(max_length=4, choices=CONDITIONS)
    remarks = models.TextField()

class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    condition = models.OneToOneField(StockCondition, on_delete=models.CASCADE)
    category = models.CharField(max_length=3, choices=CATEGORIES)

class AuditDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    auditor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    auditorname = models.CharField(max_length=256, default='auditor')
    time = models.DateTimeField()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
