from django.db import models


class OrderProduct(models.Model):
    order = models.ForeignKey('webapp.Order', related_name='order_products', on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey('webapp.Product', related_name='product_orders', on_delete=models.CASCADE, verbose_name="Продукт")
    product_quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.order} | {self.product}"

    class Meta:
        db_table = "orders_products"
        verbose_name = "Заказ_Продукт"
        verbose_name_plural = "Заказы_Продукты"
