from time import strftime, gmtime

def dateInfo(text):
	return strftime('%Y-%m-%d %H:%M:%S', gmtime()) + '|Alienware Arena Script|' + text

def main():
	dateInfo()

if (__name__ == '__main__'):
	main()
