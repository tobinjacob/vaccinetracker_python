import requests
import time
from datetime import date, datetime
from win10toast import ToastNotifier

dist = 300 #district_code
# date = 'dd-mm-yyyy'
today = date.today()
d1 = today.strftime("%d-%m-%Y")
print("date: ", d1)
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
    dist, d1)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if((each["available_capacity_dose1"] > 0) & (each["min_age_limit"] < 45)):
            counter += 1
            print(each["name"])
            print(each["pincode"])
            print(each["vaccine"])
            print(each["available_capacity_dose1"])
            toaster = ToastNotifier()
            toaster.show_toast("Vaccine available!!", icon_path="notif.ico", duration=10)
            return True
    if(counter == 0):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("No Available Slots", current_time)
        return False


while(findAvailability() != True):
    time.sleep(75)
    findAvailability()