from datetime import date
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

CONDITIONS = [
        ("GOOD", "Good"),
        ("AVRG", "Average"),
        ("BRKN", "Bad"),
]

CATEGORIES = [
        ("ELC", "Electronics"),
        ("FUR", "Furniture")
]

USER_ROLES = [
        ("ADT", "Auditor"),
        ("CDN", "Custodian"),
        ("HOD", "Head of Department")
]

LOCATIONS = [
        ("CLS_1", "Classroom 1"),
        ("LAB_1", "Laboratory 1"),
        ("LAB_2", "Laboratory 2"),
        # TODO: Add actual stuff here
]

class User(AbstractUser):
    role = models.CharField(max_length=3, choices=USER_ROLES)

    def __str__(self):
        return self.username

class AuditDetail(models.Model):
    auditor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    auditor_name = models.CharField(max_length=256, default='auditor')
    time = models.DateTimeField(default=now)
    condition = models.CharField(max_length=4, choices=CONDITIONS)
    remarks = models.TextField(null=True)

    def __str__(self):
        return 'Audit by ' + self.auditor_name + ' on ' + self.time.strftime('%d/%m/%y at %H:%M:%S')


class Stock(models.Model):
    name = models.CharField(max_length=256)
    audit_details = models.ForeignKey(AuditDetail, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=3, choices=CATEGORIES)
    description = models.TextField(null=True)
    item_code = models.CharField(max_length=64, default="AISAT/CSE/AA/BBB")
    bill_no = models.CharField(max_length=64, default="0000.00")
    purchase_date = models.DateField(default=date.today)
    location = models.CharField(max_length=5, choices=LOCATIONS, default="LAB_1")

    def __str__(self):
        return self.name

class Computer(models.Model):
    name = models.CharField(max_length=256)
    mouse = models.ForeignKey(Stock, related_name="stock_mouse", on_delete=models.CASCADE)
    keyboard = models.ForeignKey(Stock, related_name="stock_keyboard", on_delete=models.CASCADE)
    monitor = models.ForeignKey(Stock, related_name="stock_monitor", on_delete=models.CASCADE)
    cpu = models.ForeignKey(Stock, related_name="stock_cpu", on_delete=models.CASCADE)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    auditor = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=5, choices=LOCATIONS)

    def __str__(self):
        return f"{self.auditor.username}'s assignment at {self.location}"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
