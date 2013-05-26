#!/usr/bin/env python

"""web_scraper.py: Requests a web page and scrapes for email addresses"""

import urllib2
import re

EMAIL_REGEX = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")

"""requests the given url and returns the html code"""
def requestPage(url):
		"""error handling for the url"""
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
			print 'URLError = ' + str(e.reason)

"""given html code, searches it for email addresses using a regular expression"""
def emailSearch(html):
	matches = re.findall(EMAIL_REGEX, html)
	print Email Addresses =matches


def main():
	url = raw_input("Please enter a website: http://")
	emailSearch(requestPage(url))

if __name__ == "__main__":
    main()
