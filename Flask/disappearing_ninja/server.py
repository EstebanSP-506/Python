from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    return render_template('pic.html', picture="tmnt")

@app.route('/ninja/<color>')
def ninja_picture(color):
    turtles = {
        "blue" : "leonardo",
        "orange" : "michelangelo",
        "red" : "raphael",
        "purple" : "donatello",
    }
    if color in turtles:
        selected = turtles[color]
    else:
        selected = "notapril"
    return render_template('pic.html', picture=selected)

app.run(debug=True)
 