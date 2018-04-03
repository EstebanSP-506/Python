from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="super_secret_key"

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        session['red'] = request.form['red']
        session['green'] = request.form['green']
        session['blue'] = request.form['blue']
        return render_template('index.html', red=request.form['red'],green=request.form['green'],blue=request.form['blue'])
    return render_template('index.html', red=255,green=255,blue=255) 

app.run(debug=True)
 
