from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.id}_{self.title}'


class Object(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название раздела')
    articles = models.ManyToManyField(Article, through='Relationship')
    is_main = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article}_{self.object}'
