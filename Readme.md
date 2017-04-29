# Kantipur News API

A Restful API for Kantipur news

* [Live Demo](https://kanti.herokuapp.com/category/world)

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

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - HTML Parsing
* [Flask](http://flask.pocoo.org/) - Web Framework
* [Requests](http://docs.python-requests.org/en/master/) - Making HTTP Requests
* [Json](https://docs.python.org/2/library/json.html) - Jsonify the output

## License

This project is licensed under the MIT License
