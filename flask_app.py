
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello_world():
    # return "fdsfds"
    return render_template("base.html")

if __name__ == '__main__':
    app.run()