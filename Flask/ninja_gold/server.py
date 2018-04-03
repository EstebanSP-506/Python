from flask import Flask, render_template, request, redirect, session, Markup
import random, datetime
app = Flask(__name__)
app.secret_key = 'SuperSecrect'


@app.route('/')
def index():
    if "your_gold" in session:
        if session['your_gold']>=0:
            if 'reset' in session:
                session.pop('reset')
            return render_template('index.html')
        else:
            session['reset']=Markup('<a href="/reset">Reset!</a>')
            session['output'].append(tuple(("Now you are in debt! Try your luck or reset the session with the link at the end! ("+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")","lost")))
            return render_template('index.html')
    session['your_gold']=0
    session['output']=[]
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.pop('your_gold')
    session.pop('output')
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def laundry():
    if request.form['action']=="farm":
        temp=random.randint(10,20)
        session['output'].append(tuple(("You stole "+str(temp)+" golds from the "+request.form['action']+"! ("+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")","win")))
        session['your_gold']+=temp
        return redirect('/')
    if request.form['action']=="cave":
        temp=random.randint(5,10)
        session['output'].append(tuple(("You stole "+str(temp)+" golds from the "+request.form['action']+"! ("+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")","win")))
        session['your_gold']+=temp
        return redirect('/')
    if request.form['action']=="house":
        temp=random.randint(2,5)
        session['output'].append(tuple(("You stole "+str(temp)+" golds from the "+request.form['action']+"! ("+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")","win")))
        session['your_gold']+=temp
        return redirect('/')
    if request.form['action']=="casino":
        temp=random.randint(0,50)
        if random.randint(0,1) != 0:
            session['output'].append(tuple(("Entered a casino and won "+str(temp)+" golds! ("+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")","win")))
            session['your_gold']+=temp
        else:
            session['output'].append(tuple(("Entered a casino and lost "+str(temp)+" golds... Ouch... ("+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")","lost")))
            session['your_gold']-=temp
        print tuple(("Entered a casino and won "+str(temp)+" golds! ("+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")","win"))
        return redirect('/')
        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)