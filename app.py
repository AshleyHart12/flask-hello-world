import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Ashley Judah in 3308!'

@app.route('/db_test')
def deb_test():
    conn = psycopg2.connect("postgresql://flask_database_24bv_user:3qisfEWiB1nELMoC8SXlOhCyQXVG6JaG@dpg-cse42qu8ii6s738sfqs0-a/flask_database_24bv")
    conn.close()
    return "DB Test Working"