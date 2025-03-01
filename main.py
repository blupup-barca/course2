# from src.vacancy import Vacancy
from src.utils import JSONSaver
from src.parser import HeadHunterAPI
from src.filter_sort import FilterSortVacancies


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    hh_api.load_vacancies(search_query)
    hh_vacancies = hh_api.get_vacancies()

    json_saver = JSONSaver()
    json_saver.fill_in_the_file(hh_vacancies)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_word = input("Введите ключевое слово для фильтрации вакансий: ")
    filter_salary = int(input("Введите минимальную зарплат: "))

    vacancies = json_saver.read_file()

    filtered_obj = FilterSortVacancies(filter_word, filter_salary, top_n)

    filtered_by_description = filtered_obj.filter_by_description(vacancies)
    print(f"Отфильтровано {len(filtered_by_description)} вакансий по описанию")

    filtered_by_salary = filtered_obj.filter_by_salary(filtered_by_description)
    print(f"Отфильтровано {len(filtered_by_salary)} вакансий по зарплате\n")

    sorted_by_salary = filtered_obj.sort_vacancies_by_salary(filtered_by_salary)

    top_vacancies = filtered_obj.get_top_vacancies(sorted_by_salary)

    print(f"Топ {top_n} вакансий:\n{top_vacancies}\n")


if __name__ == "__main__":
    user_interaction()
