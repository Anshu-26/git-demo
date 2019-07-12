# python code for accepting data from html templates
# and sending processed data for display

from flask import Flask, render_template, request
from sqlite3 import connect

app = Flask(__name__)

@app.route('/')
def open_entry_page():
    return render_template('entry.html')

@app.route('/search4', methods=['post'])
def do_search():
    location = request.form['location']
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = set(phrase).intersection(set(letters))
    save_search_data_to_db(location,phrase,letters,result)
    return render_template('results.html', x=phrase, y=letters, z=result , p=location)

@app.route('/viewlog')
def view_all_records():
    all_records = get_all_search_records_from_db()
    return render_template('view_all_records.html', all_records=all_records)

def save_search_data_to_db(location, phrase, letters, result):
    con = connect('results_db.sql')
    sql_query = """insert into records values ("%s", "%s", "%s", "%s") """ %(location, phrase, letters, result)
    cursor = con.cursor()
    cursor.execute(sql_query)
    con.commit()

def get_all_search_records_from_db():
    con = connect('results_db.sql')
    sql_query = """select * from records"""
    cursor = con.cursor()
    cursor.execute(sql_query)
    all_records = cursor.fetchall()
    return all_records

app.run(debug=True, port=5007)