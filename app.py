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

# Setup the SQL Alchemy
ma = Marshmallow(app)
db = SQLAlchemy(app)

if __name__ == '__main__':
    # this allows it to run in debug mode
    app.run(debug=True, port=500)


class PersonalInformation(Schema):
    class Meta:
        type_ = 'personalInformation'
        self_view = 'personalInfo_one'
        self_view_kwargs = ('id' '<id>')
        self_view_many = 'personalInfo_all'

        name = fields.Str(required=True)
        address = fields.Str(required=True)
        phone_number = fields.Integer()
        github_page = fields.String(required=True)

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
