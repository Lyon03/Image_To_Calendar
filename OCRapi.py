''' 
This part of the script takes the inputted image of timetable from the given directory of pathOfImage and send a request to nanonets API, which returns a json file
This json file is converted into a dictionary with the help of json.loads and with this dictionary we create and input the data into a csv file.
'''

import requests
import json
import csv

pathOfImage = 'timetable.png'

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/df672ace-ef4c-4bd5-b514-373bf377ee44/LabelFile/'
data = {'file': open(pathOfImage, 'rb')}
response = requests.post(url, auth  = requests.auth.HTTPBasicAuth('y2gh8eWyLi2Bq1W6UTbdsj0gJIZ0JZZf', ''), files = data)
loads = json.loads(response.text)

with open('Timetable.csv','w', newline='', encoding="utf-8") as fcsv:
    row = []
    writer = csv.writer(fcsv)
    for i in range(len(loads["result"][0]['prediction'][0]['cells'])):                #15 columns
        row.append(loads["result"][0]['prediction'][0]['cells'][i]['text'])
        if len(row) == 15:
            writer.writerow(row)
            row = []