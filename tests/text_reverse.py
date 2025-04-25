from pathlib import Path
from hexlet_pytest.reverse import reverse

def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def test_reverse():
    # Читаем исходный текст из файла
    input_text = get_test_data_path("input.txt").read_text()
    
    # Читаем ожидаемый результат
    expected = get_test_data_path("expected.txt").read_text()
    
    # Переворачиваем строку функцией reverse()
    actual = reverse(input_text)
    
    # Проверяем, что результат совпадает с ожидаемым
    assert actual == expected