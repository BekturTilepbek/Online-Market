from django.db import models


class Order(models.Model):
    user = models.CharField(max_length=100, verbose_name="Имя пользователя")
    phone_number = models.CharField(max_length=100, verbose_name="Номер телефона")
    address = models.CharField(max_length=150, verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    products = models.ManyToManyField(
        'webapp.Product',
        related_name='orders',
        through='webapp.OrderProduct',
        through_fields=('order', 'product'))

    def __str__(self):
        return f"{self.pk}. {self.user} {self.phone_number} {self.address} {self.created_at}"

    class Meta:
        db_table = "orders"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
