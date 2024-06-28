import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

client = gspread.authorize(creds)

def get_sheet_data(sheet_name):
    try:
        sheet = client.open(sheet_name).sheet1  
        
        return sheet.get_all_records()
    
    except Exception as e:
        print(f"Error fetching sheet data: {e}")
        return None
