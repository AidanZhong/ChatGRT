import sqlite3
import random
from datetime import datetime

import pandas as pd


def randomly_get_from_file(filename):
    corpus = get_corpus_from_file(filename)
    print(random.choice(corpus))


def get_corpus_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        corpus = f.readlines()
        return [s.strip() for s in corpus]


class DatabaseUtils:
    @staticmethod
    def execute_query(query):
        try:
            # Connect to the database
            connection = sqlite3.connect('../Data/HAIIIIIIIIII.db')

            # Create a cursor to execute the query
            cursor = connection.cursor()
            cursor.execute(query)

            # If it’s a SELECT query, fetch the results
            if query.strip().lower().startswith("select"):
                rows = cursor.fetchall()
                return rows
            else:
                connection.commit()  # Commit for non-SELECT queries (e.g., INSERT, UPDATE)

            # Close cursor and connection
            cursor.close()
            connection.close()

        except Exception as e:
            print("Error connecting to Supabase:", e)

    @staticmethod
    def create_user_table():
        DatabaseUtils.execute_query("CREATE TABLE IF NOT EXISTS USERS ("
                                    "USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                                    "USER_NAME TEXT NOT NULL,"
                                    "LAST_VISIT_TIME TIMESTAMP NOT NULL);")

    @staticmethod
    def get_last_visit_user():
        return DatabaseUtils.execute_query("SELECT USER_NAME FROM USERS ORDER BY LAST_VISIT_TIME DESC LIMIT 1;")[0][0]

    @staticmethod
    def user_is_using(user_name):
        if DatabaseUtils.check_user_exists(user_name):
            last_visit = datetime.now()
            DatabaseUtils.execute_query(
                f"UPDATE users SET LAST_VISIT_TIME = '{last_visit}' WHERE USER_NAME = '{user_name}'")
        else:
            last_visit = datetime.now()
            DatabaseUtils.execute_query(
                f"INSERT INTO users (USER_NAME, LAST_VISIT_TIME) values ('{user_name}', '{last_visit}')")

    @staticmethod
    def check_user_exists(user_name):
        return DatabaseUtils.execute_query(f"SELECT COUNT(*) FROM USERS WHERE USER_NAME = '{user_name}'")[0][0] > 0
