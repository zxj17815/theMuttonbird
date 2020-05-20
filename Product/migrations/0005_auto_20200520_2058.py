# Generated by Django 2.2.3 on 2020-05-20 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='product',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='spec_info',
        ),
        migrations.AddField(
            model_name='stock',
            name='product_spec',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='Product.ProductSpec', verbose_name='ProductSpec'),
            preserve_default=False,
        ),
    ]