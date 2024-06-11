def create_index_for_test_text(cnx):
    cursor = cnx.cursor()
    query = "CREATE INDEX test_text_idx ON test_table(test_text)"
    cursor.execute(query)
    cnx.commit()

def drop_index_for_test_text(cnx):
    cursor = cnx.cursor()
    query = "DROP INDEX test_text_idx ON test_table"
    cursor.execute(query)
    cnx.commit()


def select_test_table_like(cnx):
    cursor = cnx.cursor()
    query = "SELECT * FROM test_table WHERE test_text LIKE %s"
    pattern = '%System%'
    cursor.execute(query, (pattern,))
    rows = cursor.fetchall()
    return rows
