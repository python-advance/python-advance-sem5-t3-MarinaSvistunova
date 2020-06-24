'''
3.2. На основе фрагмента программы, предложенного преподавателем, реализовать класс для получения данных с сайта
     Центробанка РФ с использованием сервиса, который они предоставляют. Применить шаблон проектирования «Декоратор»
     для реализации функционала, позволяющего преобразовывать данные о курсах валют в формат JSON.

3.3. Создание ЭОР на тему «Обзор современных фреймворков, реализующих шаблон архитектуры системы MVC», создание
     сравнительной таблицы 3-5 фреймворков.
'''

from urllib.request import urlopen
from xml.etree import ElementTree as ET


class BaseClass:

    def get_currencies(self) -> str:
        pass


class CurrenciesSimple(BaseClass):

    def get_currencies(self, currencies_ids_lst=None):
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


class CurrenciesJSON(BaseClass):

    def __init__(self, currencies) -> None:
        self.currencies = currencies

    def get_currencies(self, currencies_ids_lst=None):
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

    def write_json(self):
        with open('ISR-3-2.json', 'w', encoding='utf-8') as file:
            file.write(str(self.get_currencies()))


if __name__ == '__main__':
    simple_cur = CurrenciesSimple()
    json_cur = CurrenciesJSON(simple_cur)

    print(simple_cur.get_currencies())
    print(json_cur.get_currencies())

    json_cur.write_json()