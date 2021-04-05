import json
from datetime import datetime
import time

import requests

# Seria ostatnich 10 notowań kursu średniego waluty EUR w formacie JSON
lastTenURL = 'http://api.nbp.pl/api/exchangerates/rates/a/eur/last/10/?format=json'
#Seria kursów średnich EUR z przedziału dat od 2021-03-01 do 2021-03-31
dateRangeURL = 'http://api.nbp.pl/api/exchangerates/rates/a/eur/2021-03-01/2021-03-31/'

lastTenFileNme = 'ten_last_mid_gbp.csv'
dateRangeFileName = 'mid_gbp_from_date_range.csv'

def getCurrency(url, file):
    with open(file, 'w') as currencyFile:
        try:
            req_date = datetime.now()
            start_time = time.time()
            getRequest = requests.get(url)
            end_time = time.time()
            req_duration = int((end_time - start_time) * 1000)
            duration = round(req_duration)
            print('Date and time: ' + str(req_date))
            print('Request duration: ' + str(duration) + ' ms')
            data = getRequest.text
            parse = json.loads(data)
            rates = parse["rates"]
            print(parse)
            print(rates)
        except:
            print('Service unavailable')
        for counter in range(10):
            currencyFile.write(str(rates[counter]))
            currencyFile.write('\n')
            counter += 1

def getTenLastMidGBP():
    with open('ten_last_mid_gbp.csv', 'w') as currencyFile:
        try:
            req_date = datetime.now()
            start_time = time.time()
            getRequest = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/last/10/?format=json')
            end_time = time.time()
            req_duration = int((end_time - start_time) * 1000)
            duration = round(req_duration)
            print('Date and time: ' + str(req_date))
            print('Request duration: ' + str(duration) + ' ms')
            data = getRequest.text
            parse = json.loads(data)
            rates = parse["rates"]
            print(parse)
            print(rates)
        except:
            print('Service unavailable')
        for counter in range(10):
            currencyFile.write(str(rates[counter]))
            currencyFile.write('\n')
            counter += 1


def getMidGBPFromDateRange():
    with open('mid_gbp_from_date_range.csv', 'w') as currencyFile:
        try:
            req_date = datetime.now()
            start_time = time.time()
            getRequest = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/gbp/2021-03-01/2021-03-31/')
            end_time = time.time()
            req_duration = int((end_time - start_time) * 1000)
            duration = round(req_duration)
            print('Date and time: ' + str(req_date))
            print('Request duration: ' + str(duration) + ' ms')
            data = getRequest.text
            parse = json.loads(data)
            rates = parse["rates"]
            print(parse)
            print(rates)
        except:
            print('Service unavailable')
        for counter in range(len(rates)):
            currencyFile.write(str(rates[counter]))
            currencyFile.write('\n')
            counter += 1

# getTenLastMidGBP()
# getMidGBPFromDateRange()

getCurrency(lastTenURL, lastTenFileNme)
getCurrency(dateRangeURL, dateRangeFileName)