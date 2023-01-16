import pytest

# импортируем класс HobbitsPriorityStatus из файла miles.py
from miles import HobbitsPriorityStatus

class TestHobbitsPriorityStatus:

    # добавь декоратор
    @pytest.mark.parametrize(
        'hobbit, priority_status',
        [
            ['Фродо', 'Platinum'],
            ['Сэм', 'Gold'],
            ['Мэри', 'Silver'],
            ['Пиппин', 'Silver']
        ]
    )
    # передай параметры из декоратора в функцию
    def test_priority_status(self, hobbit, priority_status):
        assert HobbitsPriorityStatus().get_status(hobbit) == priority_status