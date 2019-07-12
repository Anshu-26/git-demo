# Hello World web-app
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def open_html_page():
    return render_template('input.html')

@app.route('/hello')
def open_hello_page():
    name = request.args.get('userName')
    return "Hello "+name




app.run(debug=True, port=5004)







