import sqlite3
import random
import pandas as pd
import random
from datetime import datetime, timedelta
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
    def create_flight_info_table():
        DatabaseUtils.execute_query("CREATE TABLE IF NOT EXISTS FLIGHTS_INFO ("
                                    "FLIGHT_ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                                    "ORIGIN TEXT NOT NULL,"
                                    "DESTINATION TEXT NOT NULL,"
                                    "DEPARTURE_TIME TIMESTAMP NOT NULL);")

    @staticmethod
    def insert_data(origin, destination, departure_time):
        DatabaseUtils.execute_query(f"""
        INSERT INTO FLIGHTS_INFO (ORIGIN, DESTINATION, DEPARTURE_TIME)
        VALUES ('{origin}', '{destination}', '{departure_time}')
    """)

    @staticmethod
    def generate_data():

        num_records = 2000
        start_date = datetime(2024, 12, 13, 0, 0)
        end_date = datetime(2026, 1, 15, 23, 59)

        locations = [
            "Tokyo", "Delhi", "Beijing", "Brasília", "Mexico City", "Cairo", "Dhaka",
            "Jakarta", "Islamabad", "Buenos Aires", "Abuja", "Manila", "Ankara",
            "Washington, D.C.", "Moscow", "Seoul", "Bangkok", "Kuala Lumpur", "Paris",
            "London", "Madrid", "Rome", "Berlin", "Hanoi", "Canberra", "Ottawa",
            "Riyadh", "Tehran", "Baghdad", "Nairobi", "Pretoria", "Addis Ababa", "Lima",
            "Bogotá", "Santiago", "Bangui", "Athens", "Warsaw", "Amsterdam",
            "Brussels", "Vienna", "Lisbon", "Oslo", "Stockholm", "Copenhagen",
            "Helsinki", "Reykjavik", "Zagreb", "Prague", "Budapest"]

        for i in range(num_records):
            origin = random.choice(locations)
            destination = random.choice([loc for loc in locations if loc != origin])
            departure_time = start_date + timedelta(
                seconds=random.randint(0, int((end_date - start_date).total_seconds())))
            DatabaseUtils.insert_data(origin, destination, departure_time)

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
