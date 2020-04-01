from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/") 
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/submit", methods=["POST"])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    return render_template('submit.html', first_name=first_name, last_name=last_name)

if __name__ == '__main__': 
   app.run()