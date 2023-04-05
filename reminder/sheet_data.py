"""

Gets data from the google sheet and does some basic checks to see if its a valid input.

"""


def sheet_data(service, today, SPREADSHEET_ID, RANGE_NAME):
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return

    # Takes all values and puts them into a dict to add to the json file.
    final_d = []
    for num, row in enumerate(values):
        subject = row[0] if len(row) > 0 and row[0] else 'No Subject'
        reminder = row[1] if len(row) > 1 and row[1] else 'No Reminder'
        date = row[2] if len(row) > 2 and row[2] else 'No Date Given'

        d = {'subject': subject,
             'reminder': reminder,
             'last_access': date,
             'row': num + 1
            }

        final_d.append(d)

    return final_d
