from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey(
        "webapp.Category",
        on_delete=models.RESTRICT,
        verbose_name="Категория",
        related_name="products",
        null=False,
        blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    image = models.URLField(max_length=300)

    def __str__(self):
        return f"{self.pk}. {self.name} ({self.category}): {self.price}"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
