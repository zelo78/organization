import random

from django.core.management.base import BaseCommand

from organization.factories import DivisionFactory, EmployeeFactory
from organization.models import Division, Employee


class Command(BaseCommand):
    help = "Populate DB with a few employees and divisions for testing"

    def add_arguments(self, parser):
        parser.add_argument(
            "-e",
            "--employees",
            nargs="?",
            default=40,
            type=int,
            help="Count of employees to be created, default 40",
        )
        parser.add_argument(
            "-d",
            "--divisions",
            nargs="?",
            default=10,
            type=int,
            help="Count of divisions to be created, default 10",
        )

    def handle(self, *args, **options):
        employees = options["employees"]
        divisions = options["divisions"]

        # создаём каркас
        parent = None
        for i in range(5):
            children = Division.objects.filter(head=parent)
            if children:
                child = random.choice(children)
            else:
                child = DivisionFactory(head=parent)
            parent = child

        # генерируем недостающие подразделения
        divisions_count = Division.objects.count()
        if divisions_count < divisions:
            for i in range(divisions - divisions_count):
                head = random.choice(Division.objects.all())
                DivisionFactory(head=head)

        # генерируем недостающих сотрудников
        employees_count = Employee.objects.count()
        if employees_count < employees:
            for i in range(employees - employees_count):
                EmployeeFactory()
