from typing import List

import requests
from abc import ABC, abstractmethod

from spyder.utils.external.github import ApiError


class Parser(ABC):
    """Абстрактный класс для работы с API приложений с вакансиями"""

    @abstractmethod
    def get_vacancies(self) -> List:
        """Получение вакансий"""
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self) -> None:
        """Инициализация"""
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 10}
        self.vacancies = []

    def load_vacancies(self, keyword: str) -> None:
        """Получение вакансий"""
        self.params['text'] = keyword
        while self.params.get('page') != 2:
            try:
                response = requests.get(self.url, headers=self.headers, params=self.params)
            except ApiError as e:
                print(f"Произошла ошибка {e}")
            else:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1

    def get_vacancies(self) -> List:
        """Получение вакансий"""
        return self.vacancies
