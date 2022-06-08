import os
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Entrypoint of app
app = Flask(__name__)

# Route of app
@app.route('/')
def helloWorld():
    return 'Hello World!'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ \
                os.path.join(basedir, 'db.sqlite3')
ma = Marshmallow(app)
db = SQLAlchemy(app)

if __name__ == '__main__':
    # this allows it to run in debug mode
    app.run(debug=True, port=500)


class PersonalInformationModel(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, required=True)
    address = db.Column(db.String, required=True)
    phone_number = db.Column(db.Integer)
    github_page = fields.String(required=True)

    def __init__(self, name, address, phone_number, github_page):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.github_page = github_page

class WorkHistory(Schema):
    class Meta:
        type_ = 'workHistory'
        self_view = 'workHistory_one'
        self_view_kwargs = ('id' '<id>')
        self_view_many = 'workHistory_all'

        business_name = fields.Str(required=True)
        work_duration = fields.Str(required=True)
        work_role = fields.Str(required=True)

class Traits(Schema):
    class Meta: 
        type_ = 'traits'
        self_view = 'traits_one'
        self_view_kwargs = ('id' '<id>')
        self_view_many = 'traits_all'

        characteristics = fields.Str(required=True)
        positive_habits = fields.Str(required=True)
        hobbies = fields.Str(required=True)
