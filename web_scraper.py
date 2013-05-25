#!/usr/bin/env python

"""web_scraper.py: Requests a web page and scrapes for email addresses """

import urllib2
import re
import sys

def requestPage(url):
		""" error handling for the url """
		try:
			response = urllib2.urlopen("http://" + url)
			print "Requesting page....\n"
			html = response.read()
			response.close()
			print "Successfully requested " + response.geturl() + "\n"
			return html
			
		except urllib2.HTTPError, e:
			print 'HTTPError = ' + str(e.code)

		except urllib2.URLError, e:
			print 'URlError = ' + str(e.reason)

def main():
	url = raw_input("Please enter a website: http://")
	requestPage(url)

if __name__ == "__main__":
    main()
