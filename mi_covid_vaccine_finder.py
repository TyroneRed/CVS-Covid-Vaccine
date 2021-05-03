from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import smtplib
import json
import tweepy


driver = webdriver.Chrome()

def closePopUp():
	#Waits for a popup window and closes it if it appears
	time.sleep(20)
	try:
		driver.find_element_by_class_name('acsDeclineButton').click()
	except:
		pass
#Navigates to the cvs website
driver.get('https://www.cvs.com/immunizations/covid-19-vaccine')
closePopUp()
#Selects the state from the scroll menu
driver.find_element_by_xpath("//*[@id='selectstate']/option[text()='Michigan']").click()
#find and click the link to schedule and appointment
driver.find_element(By.XPATH, '/html/body/content/div/div/div/div[4]/div/div[2]/form/div[2]/button').click()
time.sleep(2)
driver.find_element_by_link_text('Schedule an appointment now').click()

#Fills out the form and navigates to the next page 
no_positive_test = driver.find_element(By.XPATH, '//*[@id="questionnaire"]/section/ol/li[1]/fieldset/div/div[2]/label')
no_positive_test.click()
no_close_contact = driver.find_element(By.XPATH, '//*[@id="questionnaire"]/section/ol/li[2]/fieldset/div/div[2]/label')
no_close_contact.click()
no_symptoms = driver.find_element(By.XPATH, '//*[@id="questionnaire"]/section/ol/li[3]/fieldset/div/div[2]/label')
no_symptoms.click()
continue_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/button')
continue_button.click()
closePopUp()
try:
	driver.find_element(By.XPATH, '//*[@id="acsMainInvite"]/div/a[1]')
except:
	pass
driver.find_element(By.XPATH, '//*[@id="generic"]/section/div[2]/div/fieldset/div/div[1]/label').click()
driver.find_element_by_class_name("btn-control").click()

closePopUp()
#finds Michigan in the scroll list and clicks it
driver.find_element(By.XPATH, "//*[@id='jurisdiction']/option[25]").click()	
closePopUp()
driver.find_element_by_class_name("btn-control").click()


closePopUp()
#fills out the age in the form
driver.find_element_by_id("q1_0").send_keys(16)
#checks the box for consent
consent_box = driver.find_element_by_id("consentText")
driver.execute_script("arguments[0].click();", consent_box) 
#clicks the button
driver.find_element_by_class_name('btn-control').click()

closePopUp()
#clicks the button
driver.find_element_by_class_name('btn-control').click()
closePopUp()




filename = 'cvs_zip_codes.json'
with open(filename) as f:
	cvs_zip_codes = json.load(f)

for cvs_zip_code in cvs_zip_codes:
	zip_code_field = driver.find_element_by_id("address")
	zip_code_field.send_keys(cvs_zip_code)
	driver.find_element(By.XPATH, '//*[@id="generic"]/div/div/div[1]/button').click()
	closePopUp()

	available_cities = []
	for i in range(0,3):
		try:
			address_text = driver.find_element(By.XPATH, f'//*[@id="clinic-address-detail_{i}"]/address/div[2]').get_attribute("innerText")
			available_cities.append(address_text)
			zip_code_field.clear()
			time.sleep(2)
		except:
			zip_code_field.clear()
			print(f'No appointments available in zip code {cvs_zip_code}')
			time.sleep(2)

	if not available_cities:
		print('No appointments available')

	else:
		print(available_cities)

available_cities = set(available_cities)

filename = 'twitter_api_keys.json'
with open(filename) as f:
	twitter_access_dict = json.load(f)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitter_access_dict['API Key'], twitter_access_dict['API Secret Key'])
auth.set_access_token(twitter_access_dict['Access Token'], twitter_access_dict['Access Secret'])

# Create API object
api = tweepy.API(auth)

# Create a tweet
filename = 'tweeted_cities.json'
with open(filename) as f:
	tweeted_cities = json.load(f)

for city in available_cities:
	if city not in tweeted_cities:
		api.update_status(f"COVID-19 vaccine appointments available at CVS in {city}.")
		tweeted_cities.append(city)
	else:
		print(f'You already tweeted about {city}')

filename = 'tweeted_cities.json'
with open(filename, 'w') as f:
	json.dump(tweeted_cities, f)