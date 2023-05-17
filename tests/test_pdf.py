import os
import textwrap
from pypdf import PdfReader

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
# применила униваерсальный путь через новую функцию
def file_path(file_name):
    return os.path.join(PROJECT_ROOT_PATH, '../resources', file_name)

def test_pdf():
    file_to_read = file_path('docs-pytest-org-en-latest.pdf')
    reader = PdfReader(file_to_read)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)
    expected_text = textwrap.dedent("""
        pytest Documentation
        Release 0.1
        holger krekel, trainer and consultant, https://merlinux.eu/
        Jul 14, 2022
        """)

    assert text.strip() == expected_text.strip()
    assert number_of_pages == 412
