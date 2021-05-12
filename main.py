from selenium import webdriver
import unittest
import csv
import urllib
driver = webdriver.Chrome("/Users/meenakshisundaranath/Downloads/chromedriver")
driver.get("https://downtowndallas.com/experience/stay/")
driver.refresh()
driver.execute_script("window.scrollTo(0, 500)")
driver.find_element_by_xpath('/html/body/main/div/section[2]/div[1]/div[3]/a').click()
driver.execute_script("window.scrollTo(0, 500)")
name = driver.find_element_by_class_name('place-name').get_attribute("innerHTML")
address = driver.find_element_by_class_name('place-info-address').get_attribute("innerHTML")
print(name)
print(address)
myFile = open('hotel.csv', 'w')
with myFile:
    myNumbers = ['hotel', 'address']
    writer = csv.DictWriter(myFile, myNumbers)
    writer.writeheader()
with open('Logo.png', 'wb') as file:
#identify image to be captured
    l = driver.find_element_by_class_name('place-info-image').get_attribute("src")
#write file
    file.write(l.screenshot_as_png)




