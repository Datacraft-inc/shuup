# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-25 14:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import shuup.core.fields
import shuup.core.suppliers.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockAdjustment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created on')),
                ('delta', shuup.core.fields.QuantityField(decimal_places=9, default=0, max_digits=36, verbose_name='delta')),
                ('purchase_price_value', shuup.core.fields.MoneyValueField(decimal_places=9, default=0, max_digits=36)),
                ('type', enumfields.fields.EnumIntegerField(db_index=True, default=1, enum=shuup.core.suppliers.enums.StockAdjustmentType, verbose_name='type')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shuup.Product', verbose_name='product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuup.Supplier', verbose_name='supplier')),
            ],
        ),
        migrations.CreateModel(
            name='StockCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_limit', shuup.core.fields.QuantityField(decimal_places=9, default=0, editable=False, max_digits=36, verbose_name='alert limit')),
                ('logical_count', shuup.core.fields.QuantityField(decimal_places=9, default=0, editable=False, max_digits=36, verbose_name='logical count')),
                ('physical_count', shuup.core.fields.QuantityField(decimal_places=9, default=0, editable=False, max_digits=36, verbose_name='physical count')),
                ('stock_value_value', shuup.core.fields.MoneyValueField(decimal_places=9, default=0, max_digits=36)),
                ('product', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shuup.Product', verbose_name='product')),
                ('supplier', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='shuup.Supplier', verbose_name='supplier')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='stockcount',
            unique_together=set([('product', 'supplier')]),
        ),
    ]
