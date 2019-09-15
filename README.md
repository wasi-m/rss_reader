# Rss-Reader
A simple RSS Reader using Python Django

RSS-Reader is a web based platform that allows users to get the live rss feed from the entered URL.

Users can Enter the link on https://rssreaderdemo.herokuapp.com/ and the get the list of all feeds.
Then Users can also click on individual feed to get the details of feed.


Project Details
--------------------------------------------
- Backend - Python/Django
- Database - SQLite3 (Not Used)
- Frontend - Bootstrap, HTML, CSS, JavaScript, Jquery (Free package from creative tim)
- Hosted on - Heroku
- website - https://rssreaderdemo.herokuapp.com/


Setup Project
--------------------------------------------
1. Create a virtual environmnet and activate
```
$ virtualenv venv
$ source venv/bin/activate
```
2. Clone Project from https://github.com/wasi-m/rss_reader.git
```
$ git clone https://github.com/wasi-m/rss_reader.git
```
3. Install all project dependency from requirements.txt file
```
$ pip install -r requirements.txt
```
4. Go to project folder and run the Django makemigrations and migrate
```
$ python manage.py makemigrations
$ python manage.py migrate
```
5. Go to project folder and run Django development server
```
$ python manage.py runserver
```
6. Open http://127.0.0.1:8000 in browser
