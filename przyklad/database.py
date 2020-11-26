import sqlite3
from collections import OrderedDict

conn = sqlite3.connect('baza.db')


def _init_db():
    with open("schema.sql") as f:
        sql_script = f.read()
        with conn:
            conn.executescript(sql_script)


def insert_data(table_name: str, fields: OrderedDict):
    with conn:
        stmt = f"insert into '{table_name}' (" + ','.join(["'" + str(el) + "'" for el in fields.keys()]) + ") values (" + ','.join(["'" + str(el) + "'" for el in fields.values()]) + ")"
        print(stmt)
        conn.execute(stmt)


def fill_films_table(FilmID: int, FilmName: str, BoxOffice: int, Year: str) -> None:
    table_name = "Films"
    fields = OrderedDict()
    fields["FilmID"] = FilmID
    fields["FilmName"] = FilmName
    fields["BoxOffice"] = BoxOffice
    fields["Year"] = Year
    insert_data(table_name, fields)


def fill_actors_table(ActorID: int, ActorName: str):
    table_name = "Actors"
    fields = OrderedDict()
    fields["ActorID"] = ActorID
    fields["ActorName"] = ActorName
    insert_data(table_name, fields)


def fill_films_roles_table(RoleID: int, FilmID: int, RoleName: str):
    table_name = "Films_Roles"
    fields = OrderedDict()
    fields["RoleID"] = RoleID
    fields["FilmID"] = FilmID
    fields["RoleName"] = RoleName
    insert_data(table_name, fields)


def fill_actors_roles_table(ActorID: int, RoleID: int):
    table_name = "Actors_Roles"
    fields = OrderedDict()
    fields["ActorID"] = ActorID
    fields["RoleID"] = RoleID
    insert_data(table_name, fields)



_init_db()