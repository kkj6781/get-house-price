import requests
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

ZWSID = "***"
zpid = "52388704"
url = 'http://www.zillow.com/webservice/GetZestimate.htm?zws-id={}&zpid={}'.format(ZWSID, zpid)

page = requests.get(url)
tree = page.text
location = tree.find('<zestimate>')
price = tree[location + 34:location + 40]

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('House Price Example-2b118bc598d6.json', scope)
gc = gspread.authorize(credentials)
google_doc_link = 'https://docs.google.com/spreadsheets/d/1X6tRFUBAAMdEgSTU1EZBqOnaAHWSyKPOnkEzyqZfIK4/edit#gid=0'
wks = gc.open_by_url(google_doc_link).worksheet('Random House')
wks.append_row([time.strftime("%m/%d/%Y"), time.strftime("%H:%m"), price])


