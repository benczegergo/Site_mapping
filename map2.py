import time
file=open("url.txt","r")
links=open("links.txt","w")
url=file.readline()
max_depth=file.readline()
max_depth=int(max_depth)
file.close()

from selenium import webdriver


def traverse(url, depth):
	driver = webdriver.Chrome('C:/Users/bence/Dokumentumok/Map/chromedriver.exe')
	if depth > 0:				
		driver.get(url)
		ids = driver.find_elements_by_xpath('//*[@href]')
		if ids == []:
			return
		for id in ids:
			try:
				new_url=id.get_attribute('href')
				print ('###' * (max_depth - depth),)
				print(" " + new_url)
				links.write("%s %s\n" % ('\t'*(max_depth-depth),new_url))
				traverse(new_url, depth - 1)
			except:
				print("OOPS")
		else:
			return;
	else:
		driver.get(url)
		ids = driver.find_elements_by_xpath('//*[@href]')
		for id in ids:
			new_url=id.get_attribute('href')
			print ('###' * (max_depth - depth),)
			print(" " + new_url)
			links.write("%s %s\n" % ('\t'*(max_depth-depth),new_url))
	driver.close()
		


traverse(url, max_depth)

links.close()
time.sleep(4)

