from selenium import webdriver
import time
import json
"""Scrape the zip codes for all the CVS locations in Michigan and save as a list in json"""

driver = webdriver.Chrome()
#open CVS locations page for Michigan
driver.get('https://www.cvs.com/store-locator/cvs-pharmacy-locations/Michigan')

#Make a list of links on that page (one link/city)
links = driver.find_elements_by_css_selector('a[href*="cvs-pharmacy-locations"]')
#remove main website link
del links[0]

#Create a formatted list of the links
location_urls = []
for link in links:
	location_url = link.get_attribute('href')
	location_urls.append(location_url)

#visit the links and scrape the addresses of the CVS website
text_addresses = []
for location_url in location_urls:
	driver.get(location_url)
	time.sleep(2)
	store_addresses = driver.find_elements_by_class_name('store-address')
	for store_address in store_addresses:
		text_addresses.append(store_address.text)

#parse the addresses and create a list of zip codes
zip_codes= []
for text_address in text_addresses:
	zip_code = text_address[-5:]
	zip_codes.append(zip_code)


print(zip_codes)
#remove duplicate zip codes
zip_codes = set(zip_codes)
#format set back to list to save as a json file
zip_codes = list(zip_codes)
print(zip_codes)

filename = 'cvs_zip_codes.json'
with open(filename, 'w') as f:
	json.dump(zip_codes, f)


