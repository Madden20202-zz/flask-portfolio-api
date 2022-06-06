from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Imports for Abstraction Layer
from marshmallow_jsonapi.flask import Schema 
from marshmallow_jsonapi import fields

# Entrypoint of app
app = Flask(__name__)

# Setup the SQL Alchemy
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////portfolio.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    # this allows it to run in debug mode
    app.run(debug=True)

