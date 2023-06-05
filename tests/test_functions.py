from src.functions import read_operations, sorting_operations, five_transaction, mask_card_number, mask_amount_number, \
    number_bloc, transfer_date


def test_read_operations(path_to_test_json, expected_result_for_json_test):
    assert read_operations(path_to_test_json) == expected_result_for_json_test


def test_sorting_operations(data_for_sort, data_result_for_sort):
    assert sorting_operations(data_for_sort) == data_result_for_sort


def test_five_transaction(expected_result_for_json_test, expected_result_five_test):
    assert five_transaction(expected_result_for_json_test) == expected_result_five_test


def test_five_transaction_(expected_five_test_1, expected_five_test_2):
    assert five_transaction(expected_five_test_1) == expected_five_test_2


def test_mask_card_number(expected_result_five_test, mask_card_number_test):
    assert mask_card_number(expected_result_five_test) == mask_card_number_test


def test_mask_amount_number(mask_card_number_test, mask_amount_number_test):
    assert mask_amount_number(mask_card_number_test) == mask_amount_number_test


def test_mask_amount_number_(mask_amount_number_test_1, mask_amount_number_test_2):
    assert mask_amount_number(mask_amount_number_test_1) == mask_amount_number_test_2


def test_number_bloc(mask_amount_number_test, bloc_result_test):
    assert number_bloc(mask_amount_number_test) == bloc_result_test


def test_transfer_date(bloc_result_test, result_transfer_date):
    assert transfer_date(bloc_result_test) == result_transfer_date


def test_transfer_date_(result_transfer_date_1, result_transfer_date_2):
    assert transfer_date(result_transfer_date_1) == result_transfer_date_2
