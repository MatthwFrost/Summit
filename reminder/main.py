'''
Creating API access for the reminder.


GENERAL API FOR PROJECT.
MAY SPLIT IT UP IN THE FUTURE.
'''


from flask import Flask, render_template
from flask_restful import Api, Resource

# Own packages
from sheet_data import sheet_data
from gAuth import Service
from fetch_data import fetch_data
from datetime import datetime, timedelta


app = Flask(__name__)
api = Api(app)

# The ID and range of reminder spreadsheet.
SPREADSHEET_ID = "ADD THIS IN"
RANGE_NAME = 'Sheet1!A:C'
DATE_FORMAT = '%Y-%m-%d'
today = datetime.today().date()


@app.route("/")
def hello_world():
    return "<h1> Mirror Project </h1>\
            <p>Home page for the mirror project</p>\
            <p>API endpoints:</p>\
            <br><p> <br>- /reminder <br># Get the revision reminders from the google sheet</p>", 200

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "<h1>Oops, can't find what you are looking for</h1>\
            <p>You have probably just found this project burried in a file somewhere and forgot all the links</p>", 404


class Reminder(Resource):
    def get(self):

        # Call the Sheets API
        service = Service()
        final_d = sheet_data(service, today, SPREADSHEET_ID, RANGE_NAME)
        output = fetch_data(service, today, DATE_FORMAT, SPREADSHEET_ID, final_d)

        return output, 200


api.add_resource(Reminder, '/reminder')  # '/reminder' is our entry point for reminder 

if __name__ == '__main__':
    app.run()  # run our Flask app
