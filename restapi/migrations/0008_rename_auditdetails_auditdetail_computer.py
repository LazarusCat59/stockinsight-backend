# Generated by Django 5.0.2 on 2024-04-22 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_stock_bill_no_stock_item_code_stock_location_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuditDetails',
            new_name='AuditDetail',
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_cpu', to='restapi.stock')),
                ('keyboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_keyboard', to='restapi.stock')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_monitor', to='restapi.stock')),
                ('mouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_mouse', to='restapi.stock')),
            ],
        ),
    ]
