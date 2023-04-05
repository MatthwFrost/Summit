"""

Parses the data from the sheet_data and picks an array at random. Its based
off how long ago it was picked, reminder > 1 day ago .

"""


from datetime import datetime, timedelta
import random

def fetch_data(service, today, DATE_FORMAT,SPREADSHEET_ID, final_d):

    subtract_day = 1
    min_date = today - timedelta(days=subtract_day)
    output = {'subject': None, 'reminder': None}
    count = 0

    while True:
        # Choses random index and checks date.
        cont_int = random.randint(0, len(final_d) - 1)

        try:
            # Get item and find the last_access date.
            item = final_d[cont_int]
            item_date = item["last_access"]
            item_date = datetime.strptime(item_date, DATE_FORMAT).date()
        except:
            return f"Not a valid date input on row {item['row']}. Please input a date with the correct format."

        # Checks if the item date is less than min date, if so move on
        if item_date < min_date:
            reminder = item["reminder"]
            subject = item["subject"]

            access_date = datetime.strftime(today, DATE_FORMAT)

            # Update date when accessed
            row = item['row']
            cell = f'Sheet1!C{row}'
            # Update the cell value
            body = {
                'values': [
                    [access_date],
                ]
            }

            result = service.spreadsheets().values().update(
                spreadsheetId=SPREADSHEET_ID,
                range=cell,
                valueInputOption='USER_ENTERED',
                body=body).execute()
            break

        else:
            cont_int = random.randint(0, len(final_d) - 1)

            count += 1

            # Check for infinite loop
            if count == 100:
                reminder = None
                subject = None
                break

    # Add final output to list
    output['subject'] = subject
    output['reminder'] = reminder

    return output
