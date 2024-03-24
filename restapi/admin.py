from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StockCondition, Stock, AuditDetails

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Roles',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'role',
                ),
            },
        ),
    )

admin.site.register(StockCondition)
admin.site.register(User, CustomUserAdmin)
admin.site.register(AuditDetails)
admin.site.register(Stock)
