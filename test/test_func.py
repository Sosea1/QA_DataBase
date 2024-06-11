import pytest
import mysql.connector
from utils.func import select_all, create_index, drop_index


# Фикстура, создание окружения, в данном случае подключение к БД
@pytest.fixture(scope="session")
def test_db():
    connection = mysql.connector.connect(user='root', password='1234',
                                         host='localhost', database='test')
    yield connection
    connection.close()


# Тест работоспособности запроса без индекса.
def test_functional_select_no_index(test_db):
    connection = test_db
    rows_without_index = select_all(connection)
    assert len(rows_without_index) == 10079 # Заранее известное значение


# Тест работоспособности запроса с индексом.
def test_functional_select_index(test_db):
    connection = test_db
    create_index(connection)
    rows_with_index = select_all(connection)
    assert len(rows_with_index) == 10079 # Заранее известное значение
    drop_index(connection)


# Тест чтобы убедится что запросы с индексом и без индекса работают одинаково, на одних данных.
def test_functional_select_like(test_db):
    connection = test_db
    rows_without_index = select_all(connection)
    create_index(connection)
    rows_with_index = select_all(connection)
    assert len(rows_without_index) == len(rows_with_index)
    drop_index(connection)
