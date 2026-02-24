from django.core.management import call_command
from django.core.management.base import BaseCommand

from materials.models import Course, Lesson


class Command(BaseCommand):
    help = "Загрузка данных курсов и уроков"

    def handle(self, *args, **options):
        Lesson.objects.all().delete()
        Course.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Все существующие курсы и уроки удалены"))

        call_command("loaddata", "courses.json")
        self.stdout.write(self.style.SUCCESS("Фикстура курсов загружена"))

        call_command("loaddata", "lessons.json")
        self.stdout.write(self.style.SUCCESS("Фикстура уроков загружена"))
