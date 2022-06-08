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
    github_page = db.column(db.String, required=True)

    def __init__(self, name, address, phone_number, github_page):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.github_page = github_page

class WorkHistoryModel(db.model):
    id = db.Column(dbInteger, primary_key=True)
    business_name = db.Column(db.String, required=True)
    work_duration = db.Column(db.String, required=True)
    work_role = db.Column(db.String, required=True)

    def __init__(self, id, business_name, work_duration, work_role):
        self.business_name = business_name
        self.work_duration = work_duration
        self.work_role = work_role

class Traits(Schema):
    class Meta: 
        type_ = 'traits'
        self_view = 'traits_one'
        self_view_kwargs = ('id' '<id>')
        self_view_many = 'traits_all'

        characteristics = fields.Str(required=True)
        positive_habits = fields.Str(required=True)
        hobbies = fields.Str(required=True)
