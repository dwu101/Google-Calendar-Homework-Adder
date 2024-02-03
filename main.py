
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def addEvents(service, name, location, description, startDate, endDate, reminderDays):
    try:
        overrideDates = []
        for i in range(reminderDays):
            overrideDates.append({'method': 'popup', 'minutes': 1440* (i+1)})

        print('%sT09:00:00-07:00' % (startDate))

        event = {
            'summary':  "%s" % (name),
            'location': '%s' % (location),
            'description': '%s' % (description),
            
            'start': {
                'dateTime': '%sT09:00:00-00:00' % (startDate),
                'timeZone': 'America/New_York',
            },
            'end': {
                'dateTime': '%sT23:00:00-00:00'% (endDate),
                'timeZone': 'America/New_York',
            },
            
            'reminders': {
                'useDefault': False,
                'overrides': overrideDates,
            },
        }

        print(event)
        event = service.events().insert(calendarId='primary', body=event).execute()


        return (True, "")

    except Exception as error:
        return (False, error)
  

def main():
 
  creds = None
  
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:

    service = build("calendar", "v3", credentials=creds)

    events = []
    locations = []
    descriptions = []
    startDates = []
    endDates = []
    reminderDays = []

    with open("inputs.txt","r") as file:
        for line in file:
            line.strip()
            if line[0] == "E":
                if line[1] == "v":
                    temp = line[13:].replace(" ","")
                    temp = temp[:-1]
                    events.append(temp)
                else:
                   temp = line[23:].replace(" ","")
                   temp = temp[:-1]
                   endDates.append(temp)

            elif line[0] == "L":
                temp = line[9:].replace(" ","")
                temp = temp[:-1]
                temp += " "
                locations.append(temp)
            
            elif line[0] == "D":
                temp = line[12:].replace(" ","")
                temp = temp[:-1]
                temp += " "
                descriptions.append(temp)

            elif line[0] == "S":
                temp = line[25:].replace(" ","")
                temp = temp[:-1]
                startDates.append(temp)
 
            elif line[0] == "N": #number of days, last line.
                temp = line[77:].replace(" ","")
                temp = temp[:-1]
                reminderDays.append(int(temp)) 
    
    if len(events) != len(locations) or len(events) != len(descriptions) or len(events) != len(startDates) or len(events) != len(endDates) or len(events) != len(reminderDays):
        raise Exception("Error: Please make sure all parameters are present in inputs.txt, even they are left empty")

    for i in range(len(events)):
        result = addEvents(service, events[i], locations[i], descriptions[i], startDates[i], endDates[i], reminderDays[i])

        if not result[0]:
            raise Exception(result[1])

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
