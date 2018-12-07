from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from dateInfo import dateInfo
import login, getLinks, upvote


def getSiteLinks():
	return [
		'https://uk.alienwarearena.com/forums/board/440/cosplay-1',
		'https://uk.alienwarearena.com/forums/board/113/off-topic-4',
		'https://uk.alienwarearena.com/forums/board/464/in-game-media-2',
		'https://uk.alienwarearena.com/forums/board/458/gaming-news'
	]


def main(headless=True):
	# 1 Login
	loginInfo = login.getLoginInfo()

	print(dateInfo('Configuring Firefox...'))
	options = Options()
	options.headless = True

	print(dateInfo('Launching Firefox...'))
	driver = webdriver.Firefox(options=options if headless else None)

	print(dateInfo('Logging in...'))
	login.login(loginInfo, driver)

	# 2 Declare siteLinksIdx and upvCounter
	siteLinksIdx = 0
	upvCounter = upvote.getUpvCounter(driver)

	# 3 Check if upvotes == goal
	if upvCounter[0] == upvCounter[1]:
		print(dateInfo('Already upvoted 20 posts.'))

		driver.close()
		print(dateInfo('Terminated Firefox.'))

	# 4 Upvoting loop
	while upvCounter[0] < upvCounter[1]:
		print(dateInfo('Getting links...'))
		posts = getLinks.readPosts(getSiteLinks()[siteLinksIdx])
		posts = getLinks.filterPosts(posts)
		upvLinks = getLinks.getLinks(posts)

		upvote.upvote(driver, upvLinks)

		upvCounter = upvote.getUpvCounter(driver)
		siteLinksIdx += 1


if __name__ == '__main__':
	main()
