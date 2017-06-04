#!/usr/bin/python3
import time
file=open("url.txt","r")
links= open("links.txt","w")
url=file.readline()
file.close()


from selenium import webdriver
driver = webdriver.Edge('C:/Users/bence/Dokumentumok/Map/MicrosoftWebDriver.exe')
driver.get(url)

ids= driver.find_elements_by_xpath('//*[@href]')


for id in ids:
	print(id.get_attribute('href'))
	links.write(id.get_attribute('href'))
	links.write("\n")


links.close()
time.sleep(4)
driver.close()
