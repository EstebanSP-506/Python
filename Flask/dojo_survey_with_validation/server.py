from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def form_submit():
    error = 0

    if len(request.form['name'])<1:
        flash("Name cannot be empty!", category='error')
        error+=1
    if len(request.form['comments'])<1:
        flash("Comment cannot be empty!", category='error')
        error+=1
    if len(request.form['comments'])>120:
        flash("Comment cannot be more than 120 characters!", category='error')
        error+=1
    if error != 0 :
        return redirect('/')
    return render_template('result.html')

app.run(debug=True)
