from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route("/")
def outp():
    return "Hey!"

@app.route('/', methods=['POST'])
def inp():
    name=request.form['name']
    lat=request.form['lat']
    lng=request.form['lng']
    return name

if __name__ == "__main__":
    app.run()