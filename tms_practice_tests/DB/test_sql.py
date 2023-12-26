# С использованием библиотеки sqlite3 выполнить следующее
# 1. Создать базу данных, в которой есть таблица Gryffindor
# 2. В таблице есть столбцы first_name, last_name, blood_status, born. Все имеют тип text, кроме последнего - int
# 3. Заполнить данными
# Harry Potter Half-blood 1980
# Ronald Weasley Pure-blood 1979
# Hermione Granger Muggle-born 1979
# Neville Longbottom Pure-blood 1980
# Rubeus Hagrid Half-breed 1928
# 4. Написать тесты, которые:
# - находят всех, родившихся в 1980м году
# - найти, кто родился раньше всех
# - добавляют волшебника со случайными данными и проверяют его наличие в базе. Потом можно его удалить
# === Со звёздочкой ===
# - найти всех, кто не родился в 1980м году
# - найти всех полукровок (полукровка - рожденный от магла ИЛИ от другого вида ;))
import sqlite3
import pytest
from data import new_mag, person_format, Person


# 1
def test_get(db_session):
    result = db_session.execute('SELECT * FROM Gryffindor;').fetchall()
    assert len(result) == 5


def test_the_same_age(db_session):
    result = db_session.execute('select * from Gryffindor where "born" = 1980;').fetchall()
    persons = person_format(result)
    for person in persons:
        pass
        # assert by names
        assert len(persons) == 2
        # assert person.born == 1980


def test_oldest(db_session):
    result = db_session.execute('select first_name, last_name, blood_status, min(born) from Gryffindor;').fetchone()
    oldest = person_format(result)
    assert oldest.first_name == 'Rubeus'


def test_add_new_mag(db_session):
    db_session.execute(f"INSERT INTO Gryffindor VALUES ({new_mag()})")
    db_session.connection.commit()
    # test_name = db_session.execute(f'select * from Gryffindor where "first_name = {first_name}').fetchall()
    # assert test_name == mag.first_name
