import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Ashley Judah in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://flask_database_24bv_user:3qisfEWiB1nELMoC8SXlOhCyQXVG6JaG@dpg-cse42qu8ii6s738sfqs0-a/flask_database_24bv")
    conn.close()
    return "DB Test Working"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://flask_database_24bv_user:3qisfEWiB1nELMoC8SXlOhCyQXVG6JaG@dpg-cse42qu8ii6s738sfqs0-a/flask_database_24bv")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def db_inserting():
    conn = psycopg2.connect("postgresql://flask_database_24bv_user:3qisfEWiB1nELMoC8SXlOhCyQXVG6JaG@dpg-cse42qu8ii6s738sfqs0-a/flask_database_24bv")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table SuccessfullyPopulated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://flask_database_24bv_user:3qisfEWiB1nELMoC8SXlOhCyQXVG6JaG@dpg-cse42qu8ii6s738sfqs0-a/flask_database_24bv")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgresql://flask_database_24bv_user:3qisfEWiB1nELMoC8SXlOhCyQXVG6JaG@dpg-cse42qu8ii6s738sfqs0-a/flask_database_24bv")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"