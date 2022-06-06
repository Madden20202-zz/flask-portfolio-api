from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Entrypoint of app
app = Flask(__name__)

if __name__ == '__main__':
    # this allows it to run in debug mode
    app.run(debug=True)

