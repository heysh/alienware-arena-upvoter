from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidArgumentException
from num2words import num2words
from dateInfo import dateInfo

def getUpvCounter(driver):
	driver.refresh()
	
	try:
		upvCounter = driver.find_element_by_xpath('/html/body/div[2]/div[2]/table[2]/tbody/tr[2]/td[2]').get_attribute('innerHTML')
	except NoSuchElementException as e:
		print(dateInfo(str(e).strip('\n')))
		quit()
	
	upvCounter = upvCounter.split()
	
	return [int(num) for num in upvCounter if num.isdigit()]

def upvote(driver, upvLinks):
	
	for link in upvLinks:
		print(dateInfo('Getting the {} post ({})...'.format(num2words((upvLinks.index(link))+1, to='ordinal'), link)))
		
		try:
			driver.get(link)
		except InvalidArgumentException as e:
			print(dateInfo(str(e).strip('\n')))
			continue
		
		try:
			upvChevron = driver.find_element_by_xpath("//*[contains(@class, 'fa fa-chevron-up')]")
			
			if (not upvChevron.get_attribute('style')):
				upvChevron.click()
				upvCounter = getUpvCounter(driver)
				print(dateInfo('Upvoted! ({}/{})'.format(upvCounter[0], upvCounter[1])))
			else:
				print(dateInfo('Already upvoted.'))
			
			upvCounter = getUpvCounter(driver)
			
			if (upvCounter[0] == upvCounter[1]):
				print(dateInfo('Upvoting finished!'))
				
				driver.close()
				print(dateInfo('Terminated Firefox.'))
				quit()
			
		except NoSuchElementException as e:
			print(dateInfo(str(e).strip('\n')))
			continue

def main():	
	upvote(driver, upvLinks)
	
if (__name__ == '__main__'):
	main()
