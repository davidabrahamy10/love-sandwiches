import gspread # This imports the entire gspread library so we can access any function or method within it
from google.oauth2.service_account import Credentials # This imports the credentials class which is part of the google auth library. We only need the Credentials class so we don't have to import the entire library.
from pprint import pprint
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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, whick must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
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

def update_sales_worksheet(data):
    """ 
    Update sales worksheet, add new row with the list data provided.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(stock_row)


def main():
    """ 
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)


print("Welcome to Love Sandwiches Data Automation")
main()
