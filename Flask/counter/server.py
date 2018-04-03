from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def index():
    if session.get('counter'):
        print session.get('counter')
        session['counter']+=1
        return render_template('index.html', counter=session['counter'])
    print session.get('counter')
    session['counter']=1
    return render_template('index.html', counter=session['counter'])

@app.route('/plus')
def plus():
    session['counter']+=1
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter']=None
    return redirect('/')

app.run(debug=True)
 