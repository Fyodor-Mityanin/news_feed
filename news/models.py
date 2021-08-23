from django.db import models


class News(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=200,
    )

    text = models.TextField(
        'Текст',
        help_text='Текст новости',
    )

    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    image = models.ImageField(
        'Картинка',
        upload_to='news/',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        title = self.text[:15]
        return f'{title}'

    def short_text(self):
        return self.text[:150]

    short_text.short_description = 'Начало новости'
