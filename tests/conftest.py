import os

import pytest


@pytest.fixture
def expected_result_for_json_test():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }, {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }]


@pytest.fixture
def path_to_test_json():
    return os.path.join(os.path.dirname(__file__), 'test_operations.json')


@pytest.fixture
def data_for_sort():
    return [{
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }, {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }]


@pytest.fixture
def data_result_for_sort():
    return [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }]


@pytest.fixture
def expected_result_five_test():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'},
            {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
             'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
             'to': 'Счет 75651667383060284188'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
             'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
             'to': 'Счет 11776614605963066702'},
            {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
             'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]


@pytest.fixture
def mask_card_number_test():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 159683******5199',
             'to': 'Счет 64686473678894779589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 715830******6758',
             'to': 'Счет 35383033474447895560'},
            {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
             'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 197086**********8542',
             'to': 'Счет 75651667383060284188'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
             'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Счет 751068**********6952',
             'to': 'Счет 11776614605963066702'},
            {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
             'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]


@pytest.fixture
def mask_amount_number_test():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 159683******5199',
             'to': 'Счет **9589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 715830******6758',
             'to': 'Счет **5560'},
            {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
             'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 197086**********8542',
             'to': 'Счет **4188'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
             'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Счет 751068**********6952',
             'to': 'Счет **6702'},
            {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
             'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Открытие вклада', 'to': 'Счет **2431'}]


@pytest.fixture
def bloc_result_test():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 1596 83** **** 5199',
             'to': 'Счет **9589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158 30** **** 6758',
             'to': 'Счет **5560'},
            {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
             'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 1970 86** **** **** 8542',
             'to': 'Счет **4188'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
             'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Счет 7510 68** **** **** 6952',
             'to': 'Счет **6702'},
            {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
             'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Открытие вклада', 'to': 'Счет **2431'}]


@pytest.fixture
def result_transfer_date():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '26.08.2019',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 1596 83** **** 5199',
             'to': 'Счет **9589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '03.07.2019',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158 30** **** 6758',
             'to': 'Счет **5560'},
            {'id': 142264268, 'state': 'EXECUTED', 'date': '04.04.2019',
             'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 1970 86** **** **** 8542',
             'to': 'Счет **4188'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018',
             'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Счет 7510 68** **** **** 6952',
             'to': 'Счет **6702'},
            {'id': 587085106, 'state': 'EXECUTED', 'date': '23.03.2018',
             'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Открытие вклада', 'to': 'Счет **2431'}]
