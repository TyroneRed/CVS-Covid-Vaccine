# CVS-Covid-Vaccine
Created with python 3.9, tweepy 3.10.0, and selenium 3.141.0.

Registration with the twitter API is required, along with API Key, API Key Secret, Access Token and Access Token Secret. 

michigan_covid_vaccine_finder.py navigates the cvs vaccine appointment website and checks for appointments from the zip codes in the 'cvs_zip_codes.json' file.
When appointments are found, a tweet is posted on twitter with the location and the time the appointment was found. Age variable is set to 16 to find all locations with Pfizer vaccine, setting age >= 18 will find all vaccines. 

michigan.cvs.py scrapes the CVS website for the zip codes of Michigan CVS locations and stores the set as a list in a json file called 'cvs_zip_codes.json'.

To prevent too frequent retweeting of appointments, a dictionary is created for each tweeted city and stored in 'tweeted_cities.json' and checked for tweet age before retweeting.


