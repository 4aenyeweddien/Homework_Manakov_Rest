from django.db import models


class Course(models.Model):
    """Модель курса с названием, описанием и превью."""

    name = models.CharField(
        max_length=50, verbose_name="Название курса", help_text="Укажите название курса"
    )
    picture = models.ImageField(
        upload_to="course/photo",
        verbose_name="Превью курса",
        help_text="Загрузите картинку для курса",
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        """Возвращает название курса."""
        return self.name


class Lesson(models.Model):
    """Модель урока, связанная с курсом."""

    name = models.CharField(
        max_length=50, verbose_name="Название урока", help_text="Укажите название урока"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Курс",
        help_text="Выберите курс для урока",
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )

    picture = models.ImageField(
        upload_to="lesson/photo",
        verbose_name="Превью урока",
        help_text="Загрузите картинку для урока",
        blank=True,
        null=True,
    )
    video_link = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.name} ({self.course.name})"
