from flask import Flask, jsonify, request 
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import json

app = Flask(__name__) 		#Define app using Flask

# My Variables
no_of_news = 20
main_news = []

def scrape_function(category_name):
	main_news.clear()	# Emptying the main_news list
	url = "http://kathmandupost.ekantipur.com/category/" + category_name	# Defining url based on category_name parameter
	print(url)

	# Requesting and parsing the HTML
	sauce = urlopen(url).read()
	soup = bs(sauce, 'lxml')

	# Indexing the main div that contains a single article
	items = soup.find_all("div", {"class" : "item"})

	#Looping through the items object 
	for item in items[:no_of_news]:

		#Since not all articles have images we use exception handling
		img_src = item.a.img
		try:
		    result = img_src.get("data-original")
		except AttributeError: 
		    img_src = "Null"
		else:
		    img_src = img_src.get("data-original")

		x = item.find_all("div", {"class" : "wrap"})
		headline = x[0].h2.text
		source_and_date =  x[0].p.text
		source_and_date = source_and_date.split(", ")
		if(len(source_and_date) > 1):
			source = source_and_date[0]
			date = source_and_date[1]
		else:
			source = "Null"
			date = source_and_date[0]
		description = item.find_all("div", {"class": "teaser"})[0].text
		link = "http://kathmandupost.ekantipur.com" + item.a.get('href').lstrip()
		
		# Creating a dictionary
		my_news = { "Headline" : headline,
					"Date" : date,
					"Image Source": img_src,
					"source" : source,
					"Description": description,
					"Link" : link}

		# Adding the dictionary to main_news list
		main_news.append(my_news)

@app.route('/category/<string:cat_name>', methods=['GET'])
def function_name_does_not_matter(cat_name):
	scrape_function(cat_name)
	if not main_news:
		return(jsonify({"Message" : "Category not found!"}))
	else:
		return jsonify(main_news)

if __name__ == '__main__':
	app.run(debug=True, port=8080)
