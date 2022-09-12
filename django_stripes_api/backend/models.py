from django.db import models


class Item(models.Model):
    name = models.CharField(
        'Название',
        max_length=100,
        help_text='Название товара'
    )
    description = models.TextField(
        'Описание',
        help_text='Описание товара'
    )
    price = models.DecimalField(
        'Стоимость',
        max_digits=6,
        decimal_places=2,
        help_text='Стоимость товара'
    )

    def __str__(self):
        return self.name
