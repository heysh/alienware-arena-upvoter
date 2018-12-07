from selenium import webdriver
import urllib.request
from bs4 import BeautifulSoup
from dateInfo import dateInfo


def readPosts(webpage):
	try:
		response = urllib.request.urlopen(webpage)
	except ValueError as e:
		print(dateInfo('Message: ' + str(e)))
		quit()

	html = response.read()

	soup = BeautifulSoup(html, 'html.parser')
	posts = soup.find_all('a', class_='board-topic-title')

	return posts


def removePosts(posts, tag, classVal, key=0):
	while key < len(posts):
		if posts[key].find(tag,
						   class_=classVal) is not None:
			posts.pop(key)
			continue

		key += 1

	return posts


def filterPosts(posts):
	posts = removePosts(posts, 'a', 'timeago forum-time')
	posts = removePosts(posts, 'span', 'glyphicon glyphicon-pushpin text-muted')

	return posts


def getLinks(posts, domain='https://uk.alienwarearena.com'):
	upvLinks = []
	for post in posts:
		upvLinks.append(domain + post.get('href'))

	return upvLinks
