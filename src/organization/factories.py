from datetime import date

from factory import LazyAttribute, Faker
import faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyInteger, FuzzyDate

from organization.models import Division, Employee

fake = faker.Faker("ru_RU")


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee

    class Params:
        gender = FuzzyChoice(["f", "m"])

    last_name = LazyAttribute(
        lambda obj: fake.last_name_female()
        if obj.gender == "f"
        else fake.last_name_male()
    )
    first_name = LazyAttribute(
        lambda obj: fake.first_name_female()
        if obj.gender == "f"
        else fake.first_name_male()
    )
    patronymic = LazyAttribute(
        lambda obj: fake.middle_name_female()
        if obj.gender == "f"
        else fake.middle_name_male()
    )
    age = FuzzyInteger(18, 65)
    position = Faker("job", locale="ru_RU")
    date_of_employment = FuzzyDate(date(2000, 1, 1))
    wage = FuzzyInteger(8_000, 200_000, 1_000)
    division = FuzzyChoice(Division.objects.all())


class DivisionFactory(DjangoModelFactory):
    class Meta:
        model = Division

    name = Faker("sentence", nb_words=4, locale="ru_RU")
    head = FuzzyChoice(Division.objects.all())
