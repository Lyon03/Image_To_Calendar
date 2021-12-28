# Timetable_To_Calendar
The aim of this repository is to make a script which converts an image (screenshot) of the timetable of my university (VIT) to a calendar which can be synced with my personal/work google calendar with a simple click.


## Setup
This script was developed with Python 3.9.7, if you haven't installed python check out this [guide](https://www.tutorialspoint.com/how-to-install-python-in-windows)

### Installing The Required Libraries
1) Pip, a package manager for python is essential to download/upgrade the required libraries to run this script.
To check whether it is installed run ```pip --version``` in your command line (cmd), if pip is not installed make sure to install with the help of this [guide](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)
2) We will now need to install the required modules, to do so enter ```pip install -r requirements.txt``` in the cmd, which would open the requirements.txt file and install accordingly the modules neccessary.

### Setting up the APIs
There are two APIs in use for this script to run successfully
* [Nanonets](https://nanonets.com/), which is given the image of the timetable and returns a json file.
* [Google Calendar API](https://developers.google.com/calendar/api), which adds the events to the user's google calendar.

#### Setting Up Nanonets
Create an account if you don't have one in [Nanonets](https://nanonets.com/). We essentially need two things - your **API key** and **Model ID**, which need to be stored in a text file in seperate lines respectively in the same directory as your script.

i) After Logging in, create a new model by clicking on the New Model button 
![nanonetsimageoffrontpage](https://user-images.githubusercontent.com/53299215/147347071-86642fcc-8fd4-4bcc-a8a9-11191cf69b79.png)
ii) Select Tables as we are converting a jpeg/png file to a tabular format (csv)
![nanonetsTableExtractor](https://user-images.githubusercontent.com/53299215/147348882-b9dfffa6-2b40-4a28-8650-8fe7b82b361e.png)

1) <u>Getting the API Key</u>
 
  i) Click on Documentation
  ![nanonetsDocumentation](https://user-images.githubusercontent.com/53299215/147351597-27c7c42d-ba21-42ca-bdb7-b48c5c573161.png)

  ii) Click on follow this link
  ![nanonetsAPILinkFollow](https://user-images.githubusercontent.com/53299215/147351698-20f43759-b5b1-4562-9c96-f221ce5f9665.png)
  
  iii) Create a txt file named ```nanonetsInfo.txt``` and copy the API Key into first line of the text file.
  ![nanonetsAPIKeyFinal](https://user-images.githubusercontent.com/53299215/147351724-4c384948-9efb-4dd1-bd90-6feb07af304d.png)
  
2) Getting the Model ID

  i) Click Model Settings which would give you your __model ID__
  ![nanonetsModelSettings](https://user-images.githubusercontent.com/53299215/147349088-64055076-5df5-44de-bd34-7c956bd55873.png)
  
  ii) **Make sure to copy your modelID and save it in the text file named ```nanonetsInfo.txt```** in the second line 
  ![nanonetsModelId](https://user-images.githubusercontent.com/53299215/147349196-141a123d-56d5-4ed7-9fec-e13cdfa4fb39.png)
 
#### Setting Up Google Calendar API
1) Create a [google cloud account](https://cloud.google.com/) (different from a regular google account) if you don't have an existing one.
2) Go to this [link](console.cloud.google.com) where you will need to create a project and enable calendar API. 
3) Go to Credentials and create an OAuth2.0 client, in this script's case you would need to select it Desktop app and feel free to name it whatever you feel is apt.
4) After doing so, download the credentials as a json file (which is the default) and rename it to ```client_secret.json``` in the same directory/folder as the the python files.
For more information regarding this setup you may follow this [tutorial](https://support.google.com/cloud/answer/6158849?hl=en)

## Customising & Running The Code
1) Make sure to have the screenshot of the timetable in the highest quality possible in the same directory as your python files.
2) Change the value of ```pathOfImage``` to the absolute or relative path of the image, by default the name of the file is to be 'timetable.png'
3) You may change the variable ```calendarName```  to change the name of the calendar which appears in your calendar
![calendarName](https://user-images.githubusercontent.com/53299215/147529293-92ad0a5b-f65a-4d3a-964f-bf8449cde42f.png)

## Contact Me
If you face any issues or have any questions feel free to contact me on LinkedIn : www.linkedin.com/in/joel-james-318593220

