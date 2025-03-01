from src.filter_sort import FilterSortVacancies
from src.vacancies import Vacancy


def test_filter_init():
    test = FilterSortVacancies(
        filter_word="python", filter_salary=0, top_n=5
    )
    assert test.filter_word == "python"
    assert test.filter_salary == 0
    assert test.top_n == 5


def test_filter_by_description(vacancies_list_1, vacancy_1):
    test = FilterSortVacancies(
        filter_word="от 2 лет", filter_salary=0, top_n=5
    )
    assert test.filter_by_description(vacancies_list_1) == [vacancy_1]


def test_filter_by_salary(vacancies_list_1, vacancy_2):
    test = FilterSortVacancies(
        filter_word="Python", filter_salary=10000, top_n=5
    )
    assert test.filter_by_salary(vacancies_list_1) == [vacancy_2]


def test_sort_vacancies_by_salary(vacancies_list_1, vacancy_1, vacancy_2):
    test = FilterSortVacancies(
        filter_word="Python", filter_salary=10, top_n=5
    )
    assert test.sort_vacancies_by_salary(vacancies_list_1) == [vacancy_2, vacancy_1]


def test_get_top_vacancies(vacancies_list_1):
    test = FilterSortVacancies(
        filter_word="Python", filter_salary=10, top_n=5
    )
    assert (test.get_top_vacancies(vacancies_list_1)) == (
       "Вакансия номер 1:\nhttps://hh.ru/vacancy/105338726\n\nВакансия номер 2:\nhttps://hh.ru/vacancy/105338543\n\n"
   )
