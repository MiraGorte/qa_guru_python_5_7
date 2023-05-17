import os
import xlrd


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_xls():
    PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    resources_package = os.path.join(PROJECT_ROOT_PATH, '../resources', 'file_example_XLS_10.xls')

    book = xlrd.open_workbook(resources_package)
    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество столбцов {sheet.ncols}')
    print(f'Количество строк {sheet.nrows}')
    print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=0, colx=1)}')
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))
    assert book.nsheets == 1
    assert book.sheet_names() == ['Sheet1']
    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert sheet.cell_value(rowx=0, colx=1) == 'First Name'
