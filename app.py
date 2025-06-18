import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Vulnerable Flask App"

if __name__ == '__main__':
    app.run()
