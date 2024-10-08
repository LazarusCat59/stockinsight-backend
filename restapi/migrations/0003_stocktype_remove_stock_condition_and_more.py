# Generated by Django 5.0.2 on 2024-03-24 10:33

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_alter_auditdetails_auditorname'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='stock',
            name='condition',
        ),
        migrations.AddField(
            model_name='auditdetails',
            name='condition',
            field=models.CharField(choices=[('GOOD', 'Good'), ('SDMG', 'Slightly damaged'), ('BRKN', 'Broken'), ('WRKN', 'Working'), ('PWRK', 'Partially working'), ('NWRK', 'Not working')], default='WRKN', max_length=4),
        ),
        migrations.AddField(
            model_name='auditdetails',
            name='remarks',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='auditdetails',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.auditdetails'),
        ),
        migrations.AddField(
            model_name='stock',
            name='name',
            field=models.CharField(default='default', max_length=256),
        ),
        migrations.AlterField(
            model_name='auditdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='auditdetails',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 10, 33, 14, 634169)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='stock',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.stocktype'),
        ),
        migrations.DeleteModel(
            name='StockCondition',
        ),
    ]
