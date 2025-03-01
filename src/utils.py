from abc import ABC, abstractmethod
import json
from typing import List

from src.vacancy import Vacancy


class Saver(ABC):
    """Абстрактный класс для сохранения файла в разном виде"""
    @abstractmethod
    def add_vacancy(self, vacancy):
        """Добавление вакансии"""
        pass

    @abstractmethod
    def read_file(self):
        """Получение вакансии"""
        pass

    @abstractmethod
    def delete_vacancies(self):
        """Удаление вакансии"""
        pass


class JSONSaver(Saver):
    """Класс для сохранения файла в JSON и работы с ним"""
    vacancies_count = 0

    def __init__(self) -> None:
        """Инициализация"""
        self.vacancies_list = []

    def fill_in_the_file(self, vacancies_list: List) -> None:
        """Функция для записи списка вакансий в файл"""
        try:
            with open('data/vacancies.json', 'w', encoding="utf-8") as f:
                json.dump(vacancies_list, f, ensure_ascii=False)
        except (FileNotFoundError, ValueError):
            with open('data/vacancies.json', 'a+', encoding="utf-8") as f:
                json.dump(vacancies_list, f, ensure_ascii=False)
                self.vacancies_list.append(vacancies_list)

    def add_vacancy(self, vacancy: dict) -> None:
        """Добавление вакансии"""
        try:
            with open('data/vacancies.json', "r", encoding="utf-8") as json_file:
                file_data = json.loads(json_file.read())
            file_data.append(vacancy)
            self.vacancies_list.append(file_data)
            with open('data/vacancies.json', 'w', encoding="utf-8") as f:
                json.dump(file_data, f, ensure_ascii=False)
        except (FileNotFoundError, ValueError):
            with open('data/vacancies.json', 'a+', encoding="utf-8") as f:
                json.dump([vacancy], f, ensure_ascii=False)
                self.vacancies_list.append(vacancy)

    def read_file(self) -> List:
        """Получение вакансий"""
        try:
            with open('data/vacancies.json', "r", encoding="UTF-8") as json_file:
                vacancies = json.loads(json_file.read())
            self.vacancies_list = [Vacancy(i) for i in vacancies]
            return self.vacancies_list
        except (FileNotFoundError, ValueError):
            return self.vacancies_list

    def delete_vacancies(self) -> None:
        """Удаление вакансий"""
        with open('data/vacancies.json', 'w'):
            self.vacancies_list = []
            pass
