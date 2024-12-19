from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from .validators import real_age

User = get_user_model()


class Tag(models.Model):
    tag = models.CharField('Тег', max_length=20)

    def __str__(self):
        return self.tag


class Birthday(models.Model):
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField(
        'Дата рождения',
        validators=(real_age,)
    )
    image = models.ImageField('Фото', blank=True, upload_to='birthdays_images')
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте Ctrl для выбора нескольких вариантов'
    )

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})

    class Meta:
        constraints = (
                models.UniqueConstraint(
                    fields=('first_name', 'last_name', 'birthday'),
                    name='Unique person constraint',
                ),
            )
        ordering = ('id',)
