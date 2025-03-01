from src.utils import JSONSaver


def test_add_vacancy(vacancy_1):
    json_saver = JSONSaver()
    assert len(json_saver.vacancies_list) == 0
    vacancy = vacancy_1.vacancy_dict()
    json_saver.add_vacancy(vacancy)
    assert len(json_saver.vacancies_list) == 1


def test_delete_vacancy(vacancy_1, vacancy_2, vacancy_3):
    json_saver = JSONSaver()
    assert len(json_saver.vacancies_list) == 0
    vacancy = vacancy_1.vacancy_dict()
    vacancy2 = vacancy_2.vacancy_dict()
    vacancy3 = vacancy_3.vacancy_dict()
    json_saver.add_vacancy(vacancy)
    json_saver.add_vacancy(vacancy2)
    json_saver.add_vacancy(vacancy3)
    assert len(json_saver.vacancies_list) == 3
    json_saver.delete_vacancies()
    assert len(json_saver.vacancies_list) == 0
