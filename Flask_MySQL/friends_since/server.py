from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friends_db')


@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    # run query with query_db()
    friends = mysql.query_db(query)
    # pass data to our template
    return render_template('index.html', all_friends=friends)


@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (name, age, friend_since, updated_at) VALUES (:name, :age, :friend_since, NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
        'name': request.form['name'],
        'age':  request.form['age'],
        'friend_since': request.form['friend_since']
    }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
