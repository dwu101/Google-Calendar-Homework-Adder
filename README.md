# Google-Calendar-Homework-Adder

It's easy to add events to Google Calendar, but adding 5 days of notifications every time an event is added is tedious. Especially when you put loads of homework assignments into GCal

So why not spend more time than you ever will manually adding the notifications on a script that automates it :D

TO RUN:

  Make sure you have credentials.json for the Google account you want to add calendar events to
  
  IF YOU DON'T:
    Go to https://console.cloud.google.com/ and ensure you are logged into the account to which you want to add calendar events. Create a project (in the      scope section, add https://www.googleapis.com/auth/calendar). Then enable the Google Calendar API by going to the sidebar >> APIs and Services >> Library >>     Google Calendar API >> Enable. 
  
  Then follow the instructions in the "Create credentials for a service account" section at https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account 
    
    
  All events that wish to be added will be written out with the event name, start date,... on inputs.txt in the specified format. Then main.py is executed and     every event listed in inputs.txt will be added to your Google calendar. Please follow the exact format given.


P.S. Google pls change the fact that I have to code "Remind me 1440 minutes before the event" instead of "Remind me 1 day before the event" c:
