from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def index():
    if 'target' not in session:
        session['target'] = random.randint(0,100)
        session['form_action']="/guess"
        session['button_value']="Guess!"
        session['attemps']=1
    return render_template('index.html', form_action=session['form_action'], button_value=session['button_value'])

@app.route('/guess', methods=['POST'])
def guess():
    try:
        val = int(request.form['number'])
    except ValueError:
        print("That's not an int!")
        return redirect('/')

    if int(request.form['number']) != int():
        if int(request.form['number']) < session['target']:
            session['outcome'] = "Too Low!"
            session['attemps']+=1
        elif int(request.form['number']) == session['target']:
            session['outcome'] = str(session['target'])+" was the correct number!!"
            session['form_action']="/reset"
            session['button_value']="Play Again!"
        elif int(request.form['number']) > session['target']:
            session['outcome'] = "Too High!"
            session['attemps']+=1
        return redirect('/')
    else: 
        return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('target')
    session.pop('outcome')
    return redirect('/')

app.run(debug=True)
 