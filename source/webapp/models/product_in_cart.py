from django.db import models


class ProductInCart(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        on_delete=models.PROTECT,
        related_name="product_in_cart",
        verbose_name="Продукт в корзине")
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.pk}. {self.product.name} : {self.quantity}"

    class Meta:
        db_table = "products_in_cart"
        verbose_name = "Продукт в корзине"
        verbose_name_plural = "Продукты в корзине"
