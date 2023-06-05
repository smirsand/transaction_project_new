from datetime import datetime
import json


def read_operations(file_path):
    """
    Функция считывает содержимое файла 'operations.json' и возвращает его.
    :return данные ввиде списка словарей.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data_ = json.load(f)
    return data_


def sorting_operations(data: list[dict]) -> list[dict]:
    """
    Функция принимает список с данными и сортирует по успешно выполненным последним операциям,
    и сортирует по дате. Последняя выполненная операция первая в списке.
    :param data : исходные данные для сортировки
    :return : отсортированные данные
    """
    sorted_data = []
    for operation in data:
        if operation.get('state') == 'EXECUTED' and "date":
            sorted_data.append(operation)
    sorted_data.sort(key=lambda x: x["date"], reverse=True)
    return sorted_data


def five_transaction(sorted_data: list[dict]) -> list[dict]:
    """
    Функция принимает список и возвращает список из 5 элементов
    :param sorted_data: исходные данные для сортировки
    :return: 5 элементов списка
    """
    list_transaction_ = []
    count = 0
    for i in sorting_operations(sorted_data):
        count += 1
        if count > 5:
            break
        list_transaction_.append(i)
    return list_transaction_


def mask_card_number(list_transaction: list[dict]) -> list[dict]:
    """
    Заменяет нужные цифры у номера карты на *
    :param : исходные данные
    :return: маскированную строку
    """
    mask_card_number_list = []
    for i in list_transaction:
        value = i.get('from')
        if value:
            number = str(value.split(' ')[-1])
            name_transfer = str(' '.join(value.split(' ')[:-1]))
            name_transfer_and_number = number[0:6] + ('*' * (len(number) - 10)) + number[-4:]
            i['from'] = name_transfer + ' ' + name_transfer_and_number
            mask_card_number_list.append(i)
        else:
            mask_card_number_list.append(i)
    return mask_card_number_list


def mask_amount_number(list_transaction_: list[dict]) -> list[dict]:
    """
    Заменяет нужные цифры у номера счета на *
    :param : исходные данные
    :return: список с маскированной строкой номера
    """
    mask_check_number_list = []
    for i in list_transaction_:
        if 'to' in i:
            value = i['to']
            number = str(value.split(' ')[-1])
            name_transfer = str(' '.join(value.split(' ')[:-1]))
            name_transfer_and_number = '**' + number[-4:]
            i['to'] = name_transfer + ' ' + name_transfer_and_number
            mask_check_number_list.append(i)
        else:
            mask_check_number_list.append(i)
    return mask_check_number_list


def number_bloc(mask_check_number_list: list[dict]) -> list[dict]:
    """
    Разделяет номер счета или карты на блоки по 4 цифры
    :param mask_check_number_list: принимает список
    :return: возвращает список с измененными данными
    """
    bloc = []
    for i in mask_amount_number(mask_check_number_list):
        value = i.get('from')
        if value:
            number = str(value.split(' ')[-1])
            blocks = " ".join([number[j:j + 4] for j in range(0, len(number), 4)])
            name_transfer = str(' '.join(value.split(' ')[:-1]))
            i['from'] = name_transfer + ' ' + blocks
            bloc.append(i)
        else:
            bloc.append(i)
    return bloc


def transfer_date(bloc: list[dict]) -> list[dict]:
    """
    Пререводит дату в формат <число>.<месяц>.<год>
    :param bloc: принимает список
    :return: возвращает измененный список
    """
    data_list = []
    for i in bloc:
        if 'date' in i and i['date']:
            value = i['date']
            i['date'] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
            data_list.append(i)
    return data_list
