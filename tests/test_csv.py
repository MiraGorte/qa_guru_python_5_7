import csv
import os
import os.path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_csv_file():
    PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    resources_package = os.path.join(PROJECT_ROOT_PATH, '../resources', 'eggs.csv')
    with open(resources_package, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

        # делаем это чтобы сбросить файл, т.к. проверка наступает быстрее чем происходит запись в файл
        csvfile.flush()
        os.fsync(csvfile.fileno())

    with open(resources_package, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        row1 = next(csvreader)
        row2 = next(csvreader)

        assert row1 == ['Anna', 'Pavel', 'Peter']
        assert row2 == ['Alex', 'Serj', 'Yana']
