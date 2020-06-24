'''
3.1. Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с
     использованием сервиса, который они предоставляют. Применить шаблон проектирования «Одиночка» для предотвращения
     отправки избыточных запросов к серверу ЦБ РФ. Оформить решение в виде корректно работающего приложения,
     реализовать тестирование и опубликовать его в портфолио.

3.2. На основе фрагмента программы, предложенного преподавателем, реализовать класс для получения данных с сайта
     Центробанка РФ с использованием сервиса, который они предоставляют. Применить шаблон проектирования «Декоратор»
     для реализации функционала, позволяющего преобразовывать данные о курсах валют в формат JSON.

3.3. Создание ЭОР на тему «Обзор современных фреймворков, реализующих шаблон архитектуры системы MVC», создание
     сравнительной таблицы 3-5 фреймворков.
'''

from urllib.request import urlopen
from xml.etree import ElementTree as ET


def singleton(cls):
    instances = {}

    def getinstance(*args):
        if cls not in instances:
            instances[cls] = cls(*args)
        return instances[cls]
    return getinstance


@singleton
def get_currencies(currencies_ids_lst=None):
    if currencies_ids_lst is None:
        currencies_ids_lst = [
                                'R01239',
                                'R01235',
                                'R01035',
                                'R01815',
                                'R01585F',
                                'R01589',
                                'R01625',
                                'R01670',
                                'R01700J',
                                'R01710A'
        ]
    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
    result = {}
    cur_res_xml = ET.parse(cur_res_str)
    root = cur_res_xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')
        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = el.find('Value').text
            valute_cur_name = el.find('Name').text
            result[valute_id] = (valute_cur_name, valute_cur_val)
    return result


if __name__ == "__main__":
    result = get_currencies()
    for val in result:
        print('%40s%10s' % (result[val][0], result[val][1]))

    assert id(result) == id(get_currencies()), 'Not a singletone!'