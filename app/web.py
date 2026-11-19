"""HTTP routes for the customer portal."""
import sqlite3
from flask import Flask, jsonify, request
from app.diagnostics import check_host
from app.search import find_customer

app = Flask(__name__)


@app.get('/customers')
def customers():
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE customers (id INTEGER, name TEXT)')
    db.execute("INSERT INTO customers VALUES (1, 'Jane Doe')")
    return jsonify(find_customer(db, request.args.get('name', '')))


@app.get('/diagnostics')
def diagnostics():
    return check_host(request.args.get('host', ''))
