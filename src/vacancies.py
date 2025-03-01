from typing import Dict


class Vacancy:
    """Класс для вакансий"""

    __slots__ = ("name", "vacancy_id", "__salary", "description")

    def __init__(self, vac: Dict) -> None:
        """Инициализация"""
        self.name = vac["name"] if vac["name"] else "Название не указано"
        self.vacancy_id = vac["alternate_url"] if vac["alternate_url"] else "Ссылка не указана"
        self.__salary = vac["salary"]["from"] if vac["salary"] and vac["salary"]["from"] else 0
        self.description = (vac["snippet"]["responsibility"]
            if vac["snippet"] and vac["snippet"]["responsibility"]
            else "Описание отсутствует")

    @property
    def salary(self) -> float:
        """Выдать приватные атрибуты"""
        return self.__salary

    @salary.setter
    def salary(self, value: int) -> None:
        """Поменять зарплату"""
        if value <= 0 or value is None:
            print('Зарплата не указана или равна 0')
        self.__salary = value

    def vacancy_dict(self) -> dict:
        """Выдать словарь с вакансией"""
        return {'name': self.name, 'vacancy_id': self.vacancy_id, 'salary': self.salary, 'description': self.description}

    def compare_salaries(self, other) -> str:
        """Сравнение зарплат"""
        if type(other) is self.__class__:
            if self.__salary > other.__salary:
                return f'У {self.vacancy_id} зарплата больше'
            elif self.__salary < other.__salary:
                return f'У {other.vacancy_id} зарплата больше'
            else:
                return 'У вакансий одинаковые зарплаты'
        else:
            raise ValueError('Это не сравнение вакансий!')
