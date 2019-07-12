# hello web app with user-input
#@@@@@@@@@@@@@@@@@@@@@@@@@@@
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def open_input_page():
    return render_template('input.html')

@app.route('/hello', methods=['post'])
def display_the_result_page():
    userName = request.form['userName']
    password = request.form['password']

    message = 'Your userName and Password are not valid'
    if(userName == password):
        message = 'Welcome '+userName


    return render_template('result.html', x=message)


app.run(debug=True, port=5005)
