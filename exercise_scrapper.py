import sys
import os
clear = lambda: os.system('cls')
clear()

import json
import mechanize
from lxml import html
import requests
import cookielib
import urllib, urllib2
from bs4 import BeautifulSoup
import pprint
import os.path
from exercise import Exercise

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

# #############################################################################
# The following is used for getting the url list on first run
# No need to run twice, as it loads from urls.txt
# #############################################################################

if not os.path.isfile("urls.txt"):
    urls_out = open("urls.txt", "w")

    alphaUrls = [];
    urls = [];
    listResults = [];

    alphabet = list(map(chr, range(97, 123)))

    # generate list of exercise pages in alphabetical format
    for letter in alphabet:
        if letter != 'x': # no exercises starting with x
            alphaUrls.append('http://www.bodybuilding.com/exercises/list/index/selected/'+letter)

    # iterate through each page in the alphabet and collect exercise urls
    for alphaUrl in alphaUrls:
        page = browser.open(alphaUrl)

        listResults = BeautifulSoup(page.read(), "lxml").find(id="listResults")

        for exerciseName in listResults.find_all("div", {"class" : "exerciseName" }):
            exerciseUrl = exerciseName.h3.a.get('href')
            urls_out.write(exerciseUrl+"\n")
            urls.append(exerciseUrl)
            print exerciseUrl;

    urls_out.close()
# #############################################################################
# End file generation
# #############################################################################
else:
    with open("urls.txt") as f:
        urls = f.readlines()

exercises = [];

for url in urls:
    data = {}
    page = browser.open(url)

    content = BeautifulSoup(page.read(), "lxml")
    details = content.find(id="exerciseDetails")
    guideContent = content.find("div", {"class" : "guideContent"})

    name = details.h1.string.replace("\n","").strip()

    newExercise = Exercise(name)

    guide_items = [];
    guide_notes = [];

    for guide_item in guideContent.find_all("li"):
        guide_items.append(guide_item.string)
        # print guide_item.string

    newExercise.set_guide_items(guide_items)
    # data['guide_items'] = guide_items

    for guide_note in guideContent.find_all("p"):
        if not guide_note.strong:
            note_title = guide_note.strong
            # print note_title
        guide_notes.append(guide_note.string)
        # print guide_note.string

    newExercise.set_note_title(note_title)
    newExercise.set_notes(guide_notes)

    # pp.pprint(guide_items);
    # pp.pprint(guide_notes);

    # data['Exercise Name'] = name

    for span in details.find_all("span"):
        key = span.getText().split(':')[0]

        if "Login" in key:
            break

        value = span.getText().split(':')[1].replace("\n","").strip()

        # setters
        # if not mechanics type then must be general type
        if "Mechanics" in key:
            newExercise.set_mechanics(value)
        elif "Type" in key:
            newExercise.set_type(value)

        if "Equipment" in key:
            newExercise.set_equipment(value)
        if "Force" in key:
            newExercise.set_force(value)
        if "Level" in key:
            newExercise.set_level(value)
        if "Main" in key:
            newExercise.set_muscle(value)
        if "Other" in key:
            newExercise.set_other_muscles(value)
        if "Sport" in key:
            newExercise.set_sport(value)

    exercises.append(newExercise)
