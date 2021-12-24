import csv 
#Given refers to the user's timetable and empty refers to the timetable containing values of a timetable which doesn't have any courses/subjects alloted

def emptyTimetableInit(path = 'emptyTimetable.csv'):            #appending the data of the empty timetable csv file to a list and returning the list
    with open(path) as emptyTimetable:
        readerOfEmpty = csv.reader(emptyTimetable)
        dataOfEmpty = []
        for row in readerOfEmpty:
            dataOfEmpty.append(row)
    return dataOfEmpty

def timetableInit(path = 'Timetable.csv'):                      #appending the data of the user inputted timetable csv file to a list and returning the list
    with open(path) as givenTimetable:
        readerOfGiven = csv.reader(givenTimetable)
        dataOfTimetable = []
        for row in readerOfGiven:
            dataOfTimetable.append(row)
    return dataOfTimetable

def extract(dataOfEmpty, dataOfGiven):                          #The function searches for differences between the two files inorder to extract the desired data from the user inputted file
    maindata = {}
    time = {}
    for row in range(len(dataOfGiven)):                       
        for column in range(len(dataOfGiven[row])):                       
            if dataOfEmpty[row][column] != dataOfGiven[row][column] and (column != 0 or column != 1) and len(dataOfGiven[row][column]) > 5:            #Iterating through the lists and searching for differences and accounting for error by nanonets API 
                if column == 2 :                                                                                 #Using the column number, we can know which time each subject falls in which slot. Upon finding it we are adding it to a dictionary (time) which adds the time as key and value as the subject.
                    time['08:00'] = dataOfGiven[row][column]  
                elif column == 3:
                    time['08:55'] = dataOfGiven[row][column]
                elif column == 4:
                    time['09:50'] = dataOfGiven[row][column]
                elif column == 5:
                    time['10:45'] = dataOfGiven[row][column]
                elif column == 9:
                    time['14:00'] = dataOfGiven[row][column]
                elif column == 10:
                    time['14:55'] = dataOfGiven[row][column]
                elif column == 11:
                    time['15:50'] = dataOfGiven[row][column]
                elif column == 12:
                    time['16:45'] = dataOfGiven[row][column]
                elif column == 13:
                    time['17:40'] = dataOfGiven[row][column]
                elif column == 14:
                    time['18:30'] = dataOfGiven[row][column]
    
        if row == 4 or row == 5:                                                #Using the row number we can understand which day it falls into, and adding it to the final dictionary maindata where the day is the key and the time (dictionary containing time and subject name) is the va;ue of the desired dictionary.
            maindata[0] = time                                              # 0 represents monday
        elif row == 6 or row == 7:
            maindata[1] = time                                              # 1 represents tuesday
        elif row == 8 or row == 9:
            maindata[2] = time                                              # 2 represents wednesday
        elif row == 10 or row == 11:
            maindata[3] = time                                              # 3 represents thursday
        elif row == 12 or row == 13:
            maindata[4] = time                                              # 4 represents friday
        elif row == 14 or row == 15:
            maindata[5] = time                                              # 5 represents saturday
        elif row == 16 or row == 17:
            maindata[6] = time                                              # 6 represents sunday

        if row%2 == 1:                                                          #resetting variable time after every two iterations of the row as two rows are grouped to be part of single days schedule
            time = {}

    return maindata

empty = emptyTimetableInit()                                                    #calling the function defined previously
given = timetableInit()
extracted = extract(empty, given)
#print(extracted)                                                               #if an errror regarding out of index of list comes, print this for easier debugging

