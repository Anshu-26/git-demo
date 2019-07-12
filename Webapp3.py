# python code for accepting data from html templates
# and sending processed data for display

from flask import Flask, render_template, request

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

    return render_template('results.html', x=phrase, y=letters, z=result , p=location)



app.run(debug=True, port=5006)