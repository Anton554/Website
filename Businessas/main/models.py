from django.db import models


class UsRequest(models.Model):
    class Meta:
        verbose_name_plural = "Заявки"

    fname = models.CharField(max_length=40)
    phone = models.CharField(help_text='Номер', max_length=16)
    msg = models.CharField(help_text='Текст заявки', max_length=250)
    datacr = models.DateTimeField(null=True)
    datasn = models.DateTimeField(null=True)


class Services(models.Model):
    class Meta:
        verbose_name_plural = "Раздел услуги"
        verbose_name = 'Раздел услуг'

    chapter = models.CharField('Номер услуги', max_length=1000)
    title = models.TextField('Заголовок', max_length=100)
    text = models.TextField('Текст', max_length=1000)
    price = models.CharField('Цена', max_length=1000)

    def __str__(self):
        return self.title


class Staff(models.Model):
    class Meta:
        verbose_name_plural = "Раздел сотрудники"
        verbose_name = 'Раздел сотрудники'

    name = models.CharField('Имя', max_length=40)
    about = models.TextField('О сотруднике', max_length=1000)
    img = models.ImageField('Фото', help_text='Размер фото должен быть 300x450', upload_to='staff/')
    num = models.CharField('Расположение', max_length=1000)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    class Meta:
        verbose_name_plural = "Раздел отзывы"
        verbose_name = 'Отзыв'

    title = models.CharField('Название компании', max_length=100)
    text = models.TextField('Текст', max_length=5000)
    href = models.CharField('Ссылка', max_length=40)
    img = models.ImageField('Фото', help_text='Размер фото должен быть 500x500', upload_to='feedback/')

    def __str__(self):
        return self.title
