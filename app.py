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

# All the information will now be modeled, 
# and then filled in so it can be used
class PersonalInformationModel(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String("Austin Martz"))
    address = db.Column(db.String("407 W. 6th Street Okmulgee OK 74447"))
    phone_number = db.Column(db.Integer(539-286-3763))
    github_page = db.column(db.String("URL_LINK"))

    def __init__(self, name, address, phone_number, github_page):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.github_page = github_page

class WorkHistoryModel(db.model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String, required=True)
    work_duration = db.Column(db.String, required=True)
    work_role = db.Column(db.String, required=True)

    def __init__(self, id, business_name, work_duration, work_role):
        self.business_name = business_name
        self.work_duration = work_duration
        self.work_role = work_role

class TraitsModel(db.model):
    id = db.Column(db.Integer, primary_key=True)
    characteristics = db.Column(db.String, required=True)
    positive_habits = db.Column(db.String, required=True)
    hobbies = db.Column(db.String, required=True)

    def __init__(self, characteristics, positive_habits, hobbies):
        self.characteristics = characteristics
        self.positive_habits = positive_habits
        self.hobbies = hobbies


# Schema Work 
class PersonalInformationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PersonalInformationModel(name, address, phone_number, github_page)

class WorkHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkHistoryModel(id, business_name, work_duration, work_role)

class TraitsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TraitsModel(characteristics, positive_habits, hobbies)