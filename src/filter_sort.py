import re
from typing import List


class FilterSortVacancies:
    """
    Класс для фильтрации, сортировки и вывода топ вакансий
    """

    def __init__(self, filter_word, filter_salary, top_n) -> None:
        self.filter_word = filter_word
        self.filter_salary = filter_salary
        self.top_n = top_n

    def filter_by_description(self, vacancies_list: List) -> List:
        """
        Функция для фильтрации вакансий по заданному слову в описании
        """
        filtered_vacancies_list = []
        for vacancy in vacancies_list:
            if re.findall(self.filter_word, vacancy.description, re.IGNORECASE):
                filtered_vacancies_list.append(vacancy)
        return filtered_vacancies_list

    def filter_by_salary(self, vacancies_list: List) -> List:
        """
        Функция для фильтрации вакансий по заданной зарплате
        (оставляет вакансии с зарплатой выше либо равной указанной пользователем)
        """
        filtered_vacancies_list = []
        for vacancy in vacancies_list:
            if vacancy.salary >= self.filter_salary:
                filtered_vacancies_list.append(vacancy)
        return filtered_vacancies_list

    @staticmethod
    def sort_vacancies_by_salary(vacancies_list: List) -> List:
        """
        Функция для сортировки вакансий по зарплате (по убыванию)
        """
        vacancies_list.sort(key=lambda x: x.salary, reverse=True)
        return vacancies_list

    def get_top_vacancies(self, vacancies_list: List) -> str:
        """
        Функция для получения топ N вакансий (N указывает пользователь)
        """
        top_vacancies = ""
        if self.top_n < len(vacancies_list):
            for i in range(self.top_n):
                top_vacancies += (
                    f"Вакансия номер {i + 1}:\n{str(vacancies_list[i].vacancy_id)}\n\n"
                )
        else:
            for i in range(len(vacancies_list)):
                top_vacancies += (
                    f"Вакансия номер {i + 1}:\n{str(vacancies_list[i].vacancy_id)}\n\n"
                )
        return top_vacancies
