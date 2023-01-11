from django.db import models


class UsRequest(models.Model):
    class Meta:
        verbose_name_plural = "Заявки"

    fname = models.CharField(max_length=40)
    phone = models.CharField(help_text='Номер', max_length=16)
    msg = models.CharField(help_text='Текст заявки', max_length=250)
    datacr = models.DateTimeField(null=True)
    datasn = models.DateTimeField(null=True)

