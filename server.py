from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return render_template('index.html')

@app.route("/another")
def show():
    return '<h1>Yo</h1>'

@app.route("/user/<username>")
def display(username):
    return f"Hi {username}"

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()