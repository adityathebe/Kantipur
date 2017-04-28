# Kantipur News API

A Restful API for Kantipur news

![Screenshot](http://i.imgur.com/gdzunPc.png "Screenshot: JSON Response")

## Getting Started

```
git clone https://github.com/adityathebe/Kantipur.git
```
```
cd Kantipur
```
```
py kantipur.py
```

## How to use

The API is currently designed to work only for following categories
~~~
1. National
2. World
3. Entertainment
~~~
	

The server is adjusted to run on port 8080 but you can configure that.

Run the python script and visit 
```
localhost:8080/category/national
```
or
```
localhost:8080/category/world
```
or
```
localhost:8080/category/entertainment
```

## Modules Used

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Web Scrapping
* [Flask](http://flask.pocoo.org/) - Web Framework

## License

This project is licensed under the MIT License