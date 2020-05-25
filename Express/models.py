from django.db import models
import uuid

# Create your models here.
class WayBill(models.Model):
    id = models.UUIDField('Id',primary_key=True, auto_created=True, default=uuid.uuid4,
                            editable=False, help_text="string(150),唯一编码")
    order=models.ForeignKey("OrderManageMent.Order", verbose_name="Order",related_name="WayBill",null=True, blank=True, on_delete=models.CASCADE,help_text='int，外键-订单Order')
    waybill_id=models.TextField("waybill_id",null=True, blank=True,help_text='text，快递下单id')
    code=models.TextField("ExpressCode",help_text='text，快递单号')
    mold=models.IntegerField("mold",choices=((0,'手工下单'),(1, '微信物流助手下单')),default=0,help_text='int，下单类型')

    class Meta:
        verbose_name = "WayBill"
        verbose_name_plural = "WayBills"
