#!/usr/bin/python

import re
from urllib2 import urlopen
from bs4 import BeautifulSoup

# Dictionary for storing scraped images and metadata
images = {}

# Output file
output = file('output.txt','w')

# Read the html from file
soup = BeautifulSoup(open("Astronomy Picture of the Day Archive.html"))

# Extract 100 most recent links
tags = soup.find_all('a',href=re.compile("ap\d+"))[:100]

# Track progress
noTags = len(tags)
print "%i tags" % noTags
currentTag = 0

# From these pages, grab the image url, text and timestamp
for tag in tags:
	currentTag += 1
	print "Percentage complete: %.2f" % (currentTag/float(noTags) * 100)

	# Get the url for this days picutre
	link = tag.get('href')
	url = "http://apod.nasa.gov/apod/" + link

	# Get the source for that page
	source = urlopen(url).read()
	soup = BeautifulSoup(source)

	# Find the title
	title = soup.find_all('b')[0].get_text()

	# Find the timestamp
	sndPara =  soup.find_all('p')[1]
	timestamp = sndPara.get_text().split("\n")[2]

	# Find the link to the full size image
	if sndPara.a:
		link = sndPara.a.get('href')
		imageURL = "http://apod.nasa.gov/apod/" + link
	else: continue

	# Find the description text
	descriptionHTML =  soup.find_all('p')[2]

	images[link] = {'url':url, 'title':title, 'timestamp':timestamp, 'imageURL':imageURL, 'descriptionHTML':descriptionHTML}
	
output.write(str(images))

"""
	# Find the link for the smaller image
	for child in fullSizeTag.children:
		soup = BeautifulSoup(str(child))
		imgs = soup.find_all('img')
"""
