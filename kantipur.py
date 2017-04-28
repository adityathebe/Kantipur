# Scrapping ekantipur.com
#			- Aditya Thebe

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import json

# My Variables
no_of_news = 5
category = ["national","world","entertainment"]
cat = 0
url = "http://kathmandupost.ekantipur.com/category/" + category[cat]
main_news = []

print("Loading ...")
print(category[cat] + " news\n")
# Requesting and parsing the HTML
sauce = urlopen(url).read()
soup = bs(sauce, 'lxml')

# Indexing the main div that contains a single article
items = soup.find_all("div", {"class" : "item"})

for item in items[:no_of_news]:
	x = item.find_all("div", {"class" : "wrap"})
	headline = x[0].h2.text
	date =  x[0].p.text.replace("Post Report, " , "")
	description = item.find_all("div", {"class": "teaser"})[0].text
	link = "http://kathmandupost.ekantipur.com" + item.a.get('href').lstrip()
	
	print("Headline: " + headline)
	print("Date: " + date)
	print("Description: " + description)
	print("Read More: " + link)
	print("\n")

	# Creating a dictionary
	my_news = { "Headline" : headline,
				"Date" : date,
				"Description": description,
				"Link" : link}
	main_news.append(my_news)

# Writing to a JSON file

filename = "news.json"
f = open(filename, "w")
file = json.dumps(main_news)
f.write(file)
f.close()

print("Check your file!")
