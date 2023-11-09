# 

from test_database import *

database_path = '../database/tasks.db'
table_name = 'tasks'


def test_database_presence():
    assert is_database_present(database_path)

def test_database_table_presence():
    assert is_table_present(database_path, table_name)