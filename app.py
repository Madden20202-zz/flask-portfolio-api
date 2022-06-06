from flask import Flask

app = Flask(__name__)

@app.route('/personalInformation/', methods=['GET', 'Post'])

def welcome():
    return "Hello World"

if __name__ == '__main__':
    app.run(host='localhost', port=420, debug=True)

