import pytest

# импортируем класс HobbitsPriorityStatus из файла miles.py
from miles import HobbitsPriorityStatus

class TestHobbitsPriorityStatus:

    # добавь декоратор
        assert HobbitsPriorityStatus().get_status(hobbit) == priority_status