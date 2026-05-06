import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

def connect(sheet_name):
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )
    client = gspread.authorize(creds)
    return client.open(sheet_name)

def save_order(sheet, name, phone, items, total, address):
    orders = sheet.worksheet("Orders")
    orders.append_row([
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        name, phone, str(items), total, address, "Pending"
    ])
