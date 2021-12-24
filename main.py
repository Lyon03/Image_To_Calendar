'''This project is divided into 3 parts:
1) Converting the user inputted screenshot of the timetable to CSV file (OCRapi.py)
2) Extracting the desired data from the CSV file (extraction.py) into a dictionary for easy accessibility
3) Add the data into the user's calendar (which is what main.py does)'''

calendarName = "Sem1 Timetable2.0"                                 #enter the name of timetable you wish for your google acc

from datetime import *
import OCRapi
from Extraction import *
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

def setupflow():                                                #the flow setups everything inorder to get the credentials of the user
    scopes = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=scopes)
    credentials = flow.run_console()
    return credentials

def createCalendar(calendarName):                                           #This function creates the calendar for the user        
    global idOfCalendar
    calendar = {
        'summary': calendarName,
        'timeZone': 'Asia/Kolkata'
    }
    created_calendar = service.calendars().insert(body=calendar).execute()
    idOfCalendar = created_calendar['id']
    return True

def calcMondaysDate():
    '''logic:
    1) get today's date 
    2) from 1) get which day, output would be a number between 0-6 ; 0 being monday and 6 being sunday - Day
    3) subtract todays date - day = monday's date (aa-bb-cccc)
    4) take the start time from timings
    today is 3rd of december 2021, friday which is 4
    inorder to get monday I need to subtract 3/1/2021 - (4days(friday) + 1) = monday(29th November)?'''
    todaysDate = date.today()
    todaysDay = todaysDate.weekday()
    mondaysDate = todaysDate - timedelta( days = ( todaysDay + 1 ) )
    return mondaysDate

credentials = setupflow()                                                   #retrieves the credentials  
service = build('calendar','v3', credentials = credentials)                 #creating an instance
createCalendar(calendarName)

startDate = calcMondaysDate()                                                  #run setupflow() and createCalendar only in the first run

for day in range(7):
    classesCounter = 0 
    startDate = startDate + timedelta(days=1)
    timings = list((extracted[day]).keys())
    for eachTime in timings:
        classname = (extracted[day][eachTime]).split('-')[1]
        startTimeHour = int(timings[classesCounter][:2:])
        startTimeMinute = int(timings[classesCounter][3::])
        startDateTime = datetime(startDate.year, startDate.month, startDate.day, hour=startTimeHour, minute=startTimeMinute)
        endDataTime = startDateTime + timedelta(minutes=50)
        classesCounter += 1
        event = {
        'summary': classname,
        'location': 'Online Class',
        'description': 'Boring online classes',
        'start': {
        'dateTime': startDateTime.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'Asia/Kolkata',
        },
        'end': {
        'dateTime': endDataTime.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'Asia/Kolkata',
        },
        'recurrence': [
        'RRULE:FREQ=WEEKLY'
        ],
        'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'popup', 'minutes': 10},
        ],
        },
        }

        event = service.events().insert(calendarId=idOfCalendar, body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))

