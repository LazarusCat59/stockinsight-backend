from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StockCondition, Stock, AuditDetails

# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(StockCondition)
admin.site.register(AuditDetails)
admin.site.register(Stock)
