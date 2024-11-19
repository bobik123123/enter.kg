from ckeditor.fields import RichTextField
from django.db import models
from ..utilts import upload_to_common
class PageName(models.Model):
    name = models.CharField("Название страницы", max_length=50)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страница"

    def __str__(self):
        return self.name

class Info(models.Model):
    page_name = models.ForeignKey(PageName, on_delete=models.CASCADE, related_name="info")
    text = RichTextField("текст страницы", blank=True, null=True)

    class Meta:
        verbose_name = "Информационная Страница"
        verbose_name_plural = "Информационная Страница"
    def __str__(self):
        return self.page_name.name


class Blog(models.Model):
    page_name = models.ForeignKey(PageName, on_delete=models.CASCADE, related_name="blog")
    title = models.CharField("Название статьи", max_length=255, blank=True, null=True)
    text = RichTextField("Описание статьи", blank=True, null=True)
    link = models.CharField("ссылка на статью", blank=True, null=True)
    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Static(models.Model):
    image = models.ImageField("картинка", upload_to=upload_to_common, blank=True, null=True)
    text = RichTextField("текст", blank=True, null=True)
    link = models.CharField("ссылка", max_length=255, blank=True, null=True)
