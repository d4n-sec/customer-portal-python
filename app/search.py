"""Customer lookup using SQLite."""
import sqlite3


def find_customer(connection: sqlite3.Connection, name: str):
    query = "SELECT id, name FROM customers WHERE name = '" + name + "'"
    return connection.execute(query).fetchall()
