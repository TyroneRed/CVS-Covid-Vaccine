# CVS-Covid-Vaccine

michigan_covid_vaccine_finder.py navigates the cvs vaccine appointment website and checks for appointments from the zip codes in the 'cvs_zip_codes.json' file.
When appointments are found, a tweet is posted on twitter with the location and the time appointment was found.

michigan.cvs.py scrapes the CVS website for the zip codes of Michigan CVS locations stores the set as a list in a json file called 'cvs_zip_codes.json'.
Alter line 6 to change from Michigan to another state. Alternatively, create a file named 'cvs_zip_codes.json' with the zip codes stored as a list.
The list splice at line 13 is for testing purposes.

To prevent too frequent retweeting of appointments, a list is created for each tweeted city and stored in 'tweeted_cities.json'. 
clear_tweeted_cities.py can be run on a separate schedule to clear the list.

To run the code, registration with the twitter API is required, along with API Key, API Key Secret, Access Token and Acess Token Secret. 
