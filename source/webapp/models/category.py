from unidecode import unidecode
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
