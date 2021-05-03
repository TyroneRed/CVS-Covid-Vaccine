from selenium import webdriver
import time
import json

driver = webdriver.Chrome()
driver.get('https://www.cvs.com/store-locator/cvs-pharmacy-locations/Michigan')


links = driver.find_elements_by_css_selector('a[href*="cvs-pharmacy-locations"]')
del links[0]

location_urls = []
for link in links[:5]:
	location_url = link.get_attribute('href')
	location_urls.append(location_url)

text_addresses = []
for location_url in location_urls:
	driver.get(location_url)
	time.sleep(2)
	store_addresses = driver.find_elements_by_class_name('store-address')
	for store_address in store_addresses:
		text_addresses.append(store_address.text)


zip_codes= []
for text_address in text_addresses:
	zip_code = text_address[-5:]
	zip_codes.append(zip_code)


print(zip_codes)
zip_codes = set(zip_codes)
zip_codes = list(zip_codes)
print(zip_codes)

filename = 'cvs_zip_codes.json'
with open(filename, 'w') as f:
	json.dump(zip_codes, f)


