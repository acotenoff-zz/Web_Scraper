#!/usr/bin/env python

"""web_scraper.py: Requests a web page and scrapes for email addresses """

import urllib2
import re
import sys

def requestPage(page):
		print "Requesting page....\n"
		html = ""
		try: 
			html = urllib2.urlopen(page)
		except urllib2.HTTPError, e:
			print 'HTTPError = ' + str(e.code)
		except urllib2.URLError, e:
			print 'URLError = ' + str(e.reason)
		html = response.read()
		response.close()
		print "Successfully requested " + response.geturl() + "\n"

def main():
	url = raw_input("Please enter a website: ")
	requestPage(url)

if __name__ == "__main__":
    main()
