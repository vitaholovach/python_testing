import mysql.connector


class BaseRepository:
    def __init__(self):
        self.__connection = mysql.connector.connect(host="localhost", user="root", password="ua2023")
        self.cursor = self.__connection.cursor()

    def __del__(self):
        if self.__connection:
            if self.cursor:
                self.cursor.close()
            self.__connection.close()

    def create_database(self, database: str):
        self.cursor.execute(f"create database {database};")

    def use_database(self, database: str):
        self.cursor.execute(f"use {database};")

    def insert_into_table(self, table_name, columns, values):
        self.cursor.execute(f"insert into {table_name} {columns} values {values};")
        self.commit_changes()

    def commit_changes(self):
        self.__connection.commit()
