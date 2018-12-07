import getpass, base64, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidArgumentException
from dateInfo import dateInfo


def getLoginInfo():
	try:
		with open('login.json', 'r') as loginFile:
			loginInfo = json.loads(loginFile.read())

		if loginInfo['saveLogin'] == 'N':
			loginInfo = getLogin()

		return loginInfo

	except IOError:
		loginInfo = getLogin()
		loginInfo = saveLogin(loginInfo)

		return loginInfo


def getLogin():
	username = input(dateInfo('Enter your username: '))
	password = getpass.getpass(dateInfo('Enter your password: '))

	loginInfo = {
		'username': base64.b64encode(bytes(username, 'utf-8')).decode('utf-8'),
		'password': base64.b64encode(bytes(password, 'utf-8')).decode('utf-8'),
	}

	return loginInfo


def saveLogin(loginInfo):
	save = input(dateInfo('Would you like to save your username and password? (Y/N): '))

	loginInfo.update({'saveLogin': save.upper()})

	with open('login.json', 'w') as loginFile:
		loginFile.write(json.dumps(loginInfo))

	return loginInfo


def login(loginInfo, driver):
	try:
		driver.get('https://uk.alienwarearena.com/login')
	except InvalidArgumentException as e:
		print(dateInfo(str(e).strip('\n')))
		quit()

	try:
		driver.find_element_by_id('_username').send_keys(
			base64.b64decode(loginInfo['username']).decode('utf-8'))

		driver.find_element_by_id('_password').send_keys(
			base64.b64decode(loginInfo['password']).decode('utf-8'))

		driver.find_element_by_name('_login').click()
	except NoSuchElementException as e:
		print(dateInfo(str(e).strip('\n')))
		quit()

	if driver.current_url == 'https://uk.alienwarearena.com/login':
		print(dateInfo('Incorrect login details.'))
		loginInfo = getLogin()
		saveLogin(loginInfo)
		login(loginInfo, driver)

