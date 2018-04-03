from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5
import os
import binascii
import re
app = Flask(__name__)
app.secret_key = "TheWallSecrets"
mysql = MySQLConnector(app, 'the_wall_db')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    if session.get('logged') == True:
        return redirect('/success')
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():

    errors = 0
    if len(request.form['first_name']) == 0:
        flash("First name cannot be empty!", category='error')
        errors += 1
    elif len(request.form['first_name']) < 2:
        flash("First name cannot be less than 2 characters!", category='error')
        errors += 1
    elif len(request.form['first_name']) >= 2:
        if not request.form['first_name'].isalpha():
            flash("First name can only be letters!", category='error')
            errors += 1

    if len(request.form['last_name']) == 0:
        flash("Last name cannot be empty!", category='error')
        errors += 1
    elif len(request.form['last_name']) < 2:
        flash("Last name cannot be less than 2 characters!", category='error')
        errors += 1
    elif len(request.form['last_name']) >= 2:
        if not request.form['last_name'].isalpha():
            flash("Last name can only be letters!", category='error')
            errors += 1

    if len(request.form['email']) < 1:
        flash("Email cannot be empty!", category='error')
        errors += 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", category='error')
        errors += 1

    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters!", category='error')
        errors += 1
    elif len(request.form['password']) >= 8:
        if request.form['password'] != request.form['pwd_confirmation']:
            flash("Password and Password Confirmation must match!", category='error')
            errors += 1

    if errors > 0:
        return redirect('/')
    else:

        user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
        query_data = {'email': request.form['email']}
        user = mysql.query_db(user_query, query_data)
        if len(user) != 0:
            flash("This email address is already registered!", category='warning')
            return redirect('/')
        # Write query as a string. Notice how we have multiple values
        # we want to insert into our query.
        query = "INSERT INTO users (email, first_name, last_name, password, salt, updated_at) VALUES(:email, :first_name, :last_name, :password, :salt, NOW())"

        password = request.form['password']
        salt = binascii.b2a_hex(os.urandom(15))

        hashed_pw = md5.new(password + salt).hexdigest()
        # We'll then create a dictionary of data from the POST data received.
        data = {
            'email':  request.form['email'],
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'password': hashed_pw,
            'salt': salt,
        }
        print data
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        session['success'] = 'Successfully registered your user!'
        session['logged'] = user[0]['id']
        return redirect('/success')
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():

    password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': request.form['email']}
    user = mysql.query_db(user_query, query_data)
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_password:
            session['success'] = 'Successfully logged in!!'
            print "success!!"
            # this means we have a successful login!
            session['logged'] = user[0]['id']
            return redirect('/success')
        else:
            print 'wrong email'
            flash('Wrong credentials', category='error')
            return redirect('/')
            # invalid password!
    else:
        print 'wrong email'
        flash('Wrong credentials', category='error')
        return redirect('/')
        # invalid email!
    return redirect('/')


@app.route('/success')
def success():
    if session.get('logged') == True:
        user_query = "SELECT id, CONCAT(first_name,' ',last_name) as Name, email FROM users WHERE users.id = :id LIMIT 1"
        query_data = {'id': session['logged']}
        return render_template('success.html', userdata=mysql.query_db(user_query, query_data))
    flash('You are not logged in yet! Please register or login using your credentials!', category='error')
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('logged')
    return redirect('/')


app.run(debug=True)
