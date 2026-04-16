from flask import Flask

# creating the app instance
app = Flask(__name__)

@app.route('/',)
def home():
    return '<h2>Flask Mastery Series</h2>'

@app.route("/my_name")
def my_name():
    return '<h2>Nawe</h2>'

if __name__ =="__main__":
    app.run(debug = True)
