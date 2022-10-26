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





def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")  

        sales_data = data_str.split(",") # The split method returns the data taken from data_str as a list. In order to insert the data into our spreadsheet the values need to first be in a list.
        
        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data



def validate_data(values):
    """ 
    Inside the try, converts all string values into intergers.
    Raises ValueError if strings cannot be converted into int,
    or if ther aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

data = get_sales_data()
