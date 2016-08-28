import mechanize
from lxml import html
import requests
import cookielib
import urllib, urllib2
from bs4 import BeautifulSoup
import pprint

pp = pprint.PrettyPrinter(indent=4)

browser = mechanize.Browser()
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)

browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
browser.addheaders = [('User-agent', 'WatcherBot')]

page = browser.open('http://www.bodybuilding.com/exercises/detail/view/name/pushups')

details = BeautifulSoup(page.read(), "lxml").find(id="exerciseDetails")

data = {}

name = details.h1.string.replace("\n","").strip()
data['Exercise Name'] = name

for span in details.find_all("span"):
    key = span.getText().split(':')[0]
    value = span.getText().split(':')[1].replace("\n","").strip()
    data[key] = value

pp.pprint(data)
