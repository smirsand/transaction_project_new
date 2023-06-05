from src.functions import read_operations, sorting_operations, five_transaction, mask_card_number, mask_amount_number, \
    number_bloc, transfer_date


def main():
    if __name__ == '__main__':
        reading_a_file = read_operations('operations.json')  # Чтение файла
        file_sorting = sorting_operations(reading_a_file)  # Сортировка файла
        return_five_transaction = five_transaction(file_sorting)  # Возвращение 5 транзакций
        mask_card = mask_card_number(return_five_transaction)  # Маскировка номера отправления тразакции
        mask_amount = mask_amount_number(mask_card)  # Маскировка номера принятия тразакции
        blocs_number_card = number_bloc(mask_amount)  # Разделение номера на блоки по 4 цифры
        new_list_transactions = transfer_date(blocs_number_card)  # Новый список из 5 последних выполненных транзакций

        for i in new_list_transactions:
            print(f"{i['date']} {i['description']}")
            print(f"{'' if 'from' not in i else i['from']} -> {i['to']}")
            print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print()


main()
