import pytest
import mysql.connector
from utils.func import select_test_table_like, create_index_for_test_text, drop_index_for_test_text

@pytest.fixture(scope="session", autouse=True)
def test_db():
    cnx = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='test')
    yield cnx
    cnx.close()

def test_select_test_table_like(test_db):
    cnx = test_db
    rows_without_index = select_test_table_like(cnx)
    create_index_for_test_text(cnx)
    rows_with_index = select_test_table_like(cnx)
    assert len(rows_without_index) == len(rows_with_index)
    drop_index_for_test_text(cnx)