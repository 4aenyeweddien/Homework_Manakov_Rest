from django.core.management.base import BaseCommand
from django.core.management import call_command
from users.models import User, Payment


class Command(BaseCommand):
    help = "Загрузка данных пользователей и платежей"

    def handle(self, *args, **options):
        Payment.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        self.stdout.write(
            self.style.SUCCESS("Все существующие пользователи и платежи удалены")
        )

        call_command("loaddata", "users.json")
        self.stdout.write(self.style.SUCCESS("Фикстура пользователей загружена"))

        call_command("loaddata", "payments.json")
        self.stdout.write(self.style.SUCCESS("Фикстура платежей загружена"))