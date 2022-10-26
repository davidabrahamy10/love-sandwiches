# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread # This imports the entire gspread library so we can access any function or method within it
from google.oauth2.service_account import Credentials # This imports the credentials class which is part of the google auth library. We only need the Credentials class so we don't have to import the entire library.
# Now that we have our library the next thing is to set our SCOPE.
SCOPE = [ #This is a constant because the insides of this list will never change. In Python constant variable names are written in capitals.
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)