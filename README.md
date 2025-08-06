# URLShorter
Django based URL Shortening App

This app is used to shorten long web urls to hash based urls which are easy to share.

Steps to start the app:

1. cd into the path URLShorter\URLShortening\URLShorter
2. Type python manage.py runserver
3. It will open the application with localhost IP at port 8000
4. It will ask you to click on the button to start the URL Shortening
5. Upon clicking the button, URL Shortening page will open
6. You need to input the original url and click "Submit"
7. It will generate a hash version of the input url , which will redirect you to the same original url. At the same time, it will store the mappings too.


Unittesting also can be done with the app. For that, you need to type python manage.py tests
