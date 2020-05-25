# Generated by Django 2.2.3 on 2020-05-25 21:22

import OrderManageMent.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, help_text='string(150),唯一编码', primary_key=True, serialize=False, verbose_name='Id')),
                ('out_trade_no', models.CharField(help_text='string，外部支付单号（如微信平台商户订单号）', max_length=50, verbose_name='OutTradeNo')),
                ('platform', models.IntegerField(choices=[(0, '微信小程序'), (1, 'WEB')], default=0, verbose_name='Platform')),
                ('address', models.TextField(help_text='收货信息', verbose_name='Address')),
                ('total_price', models.FloatField(help_text='总价', verbose_name='TotalPrice')),
                ('extra', models.TextField(blank=True, help_text='备注', null=True, verbose_name='Extra')),
                ('state', models.IntegerField(choices=[(0, '待付款'), (1, '待发货'), (2, '待确认'), (3, '退货中'), (4, '退款中'), (5, '已完成')], default=0, help_text='int，订单状态[0:待付款,1:待发货,2:待确认,3:退货中,4:退款中,5:已完成]', verbose_name='State')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='CreateTime')),
                ('edit_time', models.DateTimeField(auto_now=True, help_text='编辑时间', null=True, verbose_name='EditTime')),
                ('receive_time', models.DateTimeField(blank=True, help_text='退货时间', null=True, verbose_name='ReceiveTime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderPackage',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, help_text='string(150),唯一编码', primary_key=True, serialize=False, verbose_name='Id')),
                ('quantity', models.IntegerField(help_text='数量', verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_package', to='OrderManageMent.Order', verbose_name='Order')),
                ('procuct_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_package', to='Product.ProductSku', verbose_name='ProductSKU')),
            ],
            options={
                'verbose_name': 'OrderPackge',
                'verbose_name_plural': 'OrderPackges',
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, help_text='string(150),唯一编码', primary_key=True, serialize=False, verbose_name='Id')),
                ('out_refund_no', models.CharField(blank=True, help_text='string，退款单号', max_length=50, null=True, verbose_name='OutRefundNo')),
                ('extra', models.TextField(help_text='退货理由', verbose_name='Extra')),
                ('images', models.ImageField(blank=True, help_text='退货附图', null=True, upload_to=OrderManageMent.models.user_directory_path, verbose_name='Image')),
                ('price', models.FloatField(help_text='待退款金额', verbose_name='Price')),
                ('refund_type', models.IntegerField(choices=[(0, '仅退款'), (1, '退货退款')], default=0, help_text='int，退回类型[0:仅退款,1:退货退款]', verbose_name='RefundType')),
                ('state', models.IntegerField(choices=[(0, '待通过'), (1, '待退货'), (2, '待确认'), (3, '已完成'), (4, '未通过')], default=0, help_text='int，状态[0:待通过,1:待退货,2:待确认,3:已完成,4:未通过]', verbose_name='State')),
                ('re_extra', models.TextField(blank=True, help_text='商家答复信息', null=True, verbose_name='ReExtra')),
                ('customer_express', models.TextField(blank=True, help_text='text，客户寄出的快递单号', null=True, verbose_name='CustomerExpress')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='CreateTime')),
                ('edit_time', models.DateTimeField(auto_now=True, null=True, verbose_name='EditTime')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refund', to='OrderManageMent.Order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Refund',
                'verbose_name_plural': 'Refunds',
            },
        ),
        migrations.CreateModel(
            name='RefundPackage',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, help_text='string(150),唯一编码', primary_key=True, serialize=False, verbose_name='Id')),
                ('quantity', models.IntegerField(help_text='数量', verbose_name='Quantity')),
                ('order_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refund_package', to='OrderManageMent.OrderPackage', verbose_name='OrderPackage')),
                ('refund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refund_package', to='OrderManageMent.Refund', verbose_name='Refund')),
            ],
            options={
                'verbose_name': 'RefundPackage',
                'verbose_name_plural': 'RefundPackages',
            },
        ),
    ]
