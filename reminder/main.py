'''
Creating API access for the reminder.


GENERAL API FOR PROJECT.
MAY SPLIT IT UP IN THE FUTURE.
'''


from flask import Flask
from flask_restful import Api, Resource
import os

# Own packages
from sheet_data import sheet_data
from gAuth import Service
from fetch_data import fetch_data
from datetime import datetime, timedelta


app = Flask(__name__)
api = Api(app)

# The ID and range of reminder spreadsheet.
#SPREADSHEET_ID = '1FSo-4gM_2KGLDm_3EuCffY4-9gcQHtchhf4rPd626JM'
SPREADSHEET_ID = os.environ.get('SPREADSHEET')
RANGE_NAME = 'Sheet1!A:C'
DATE_FORMAT = '%Y-%m-%d'
today = datetime.today().date()

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
