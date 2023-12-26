import pytest
import sqlite3


@pytest.fixture
def db_session():
    connection = sqlite3.connect('tmsdb.db')
    db_session = connection.cursor()
    db_session.execute(
        "CREATE TABLE IF NOT EXISTS Gryffindor(first_name text, last_name text, blood_status text, born int)")  # 3
    result = db_session.fetchall()
    if result:
        pass
    else:
        db_session.execute("""
                    INSERT INTO Gryffindor VALUES
                        ('Harry', 'Potter', 'Half-blood', 1980),
                        ('Ronald', 'Weasley', 'Pure-blood', 1979),
                        ('Hermione', 'Granger', 'Muggle-born', 1979),
                        ('Neville', 'Longbottom', 'Pure-blood', 1980),
                        ('Rubeus', 'Hagrid', 'Half-breed', 1928)
                            """)
        db_session.connection.commit()
    yield db_session
    db_session.execute("DROP TABLE IF EXISTS Gryffindor")
    connection.close()



