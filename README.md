# EdTech - Online Education Platform
# Introduction
EdTech is an online learning platform built using Django that enables users to buy and watch courses. It provides dynamic connectivity with a SQLite database, allowing administrators to manage course information easily. The platform integrates payment functionality through Razorpay, allowing users to purchase courses securely. Additionally, it features user authentication with login, logout, registration, and password recovery functionalities.
# Features
**Course Management** : Admins can add, delete, and update course information dynamically through the Django admin panel. <br>
**Course Purchasing** : Users can buy courses and access them for viewing.<br>
**Payment Integration** : Payment processing is handled through Razorpay API, ensuring secure transactions.<br>
**SQLite Database** : The project utilizes SQLite as its database backend, offering scalability and reliability.
# Installation
**Navigate to the project directory** : ``` cd EdTech ``` <br>
**Run migrations to set up the database** :``` python manage.py migrate ``` <br>
**Create a superuser to access the Django admin panel** :``` python manage.py createsuperuser ```<br>
**Start the development server** : ``` python manage.py runserver ```
# Usage
1.) Access the Django admin panel by navigating to http://127.0.0.1:8000/admin in your web browser.<br>
2.) Log in with the superuser credentials created earlier.<br>
3.) Add, delete, or update course information as needed.<br>
4.) Users can visit the site, browse available courses, purchase them, and start learning.

# Technologies Used
1.) HTML<br>
2.) CSS <br>
3.) JavaScript<br>
4.) Django <br>
5.) SQLite<br>
6.) Python
