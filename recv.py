from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=["GET", 'POST'])
def index():
    print(json.dumps(request.form))
    return "App is running."

if __name__ == '__main__':
    app.run(debug=True)
