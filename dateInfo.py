import datetime


def dateInfo(text):
	return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '|Alienware Arena Script|' + text
