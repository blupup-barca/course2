from src.vacancies import Vacancy

import pytest


def test_vacancies_init(vacancy_1, vacancy_2):
    assert vacancy_1.name == "Junior Python Developer"
    assert vacancy_1.vacancy_id == "https://hh.ru/vacancy/105338726"
    assert vacancy_1.salary == 0
    assert vacancy_1.description == "Требования: опыт работы от 2 лет..."
    assert vacancy_2.name == "Junior Python Developer"
    assert vacancy_2.vacancy_id == "https://hh.ru/vacancy/105338543"
    assert vacancy_2.salary == 10000
    assert vacancy_2.description == "Требования: опыт работы от 1 лет..."


def test_setter_salary(vacancy_1):
    assert vacancy_1.salary == 0
    vacancy_1.salary = 100000
    assert vacancy_1.salary == 100000


def test_vacancies_create():
    vacancy = {"name": "Go Developer",
            "alternate_url": "https://hh.ru/vacancy/123567",
            "salary": {"from": 150000},
            "snippet": {"responsibility": "Требования: опыт работы от 3 лет..."}
    }
    vacancy = Vacancy(vacancy)
    vacancy.name = "Go Developer"
    vacancy.vacancy_id = "https://hh.ru/vacancy/123567"
    vacancy.salary = 150000
    vacancy.description = "Требования: опыт работы от 3 лет..."

def test_compare_salaries(vacancy_1, vacancy_2):
    assert vacancy_1.compare_salaries(vacancy_2) == 'У https://hh.ru/vacancy/105338543 зарплата больше'

def test_compare_salaries_error(vacancy_1):
    with pytest.raises(ValueError) as exc_info:
        assert vacancy_1.compare_salaries(1)
    assert str(exc_info.value) == "Это не сравнение вакансий!"

def test_dict(vacancy_1):
    assert vacancy_1.vacancy_dict() == {'name': "Junior Python Developer", 'vacancy_id': "https://hh.ru/vacancy/105338726", 'salary': 0, 'description': "Требования: опыт работы от 2 лет..."}
