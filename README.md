# weblog-django

## Overview
This is a weblog project built using Django framework, Bootstrap, jQuery, and class-based views. The project allows users to sign up, log in, delete their account, change profile information, view, search, create, and update posts. Authenticated users can also leave comments on post detail pages.

## Requirements
* [Python](https://www.python.org/) 3.10 or above
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [jQuery](https://jquery.com/)


## Installation

### Clone the repository:
```bash
git clone https://github.com/sinasezza/weblog-django.git
```

### Navigate to the project directory:
```bash
cd weblog_project
```

### Create a virtual Environment(optional):
__Mac/Linux users__
```bash
python3 -m venv venv
source ./venv/bin/activate
```
__Windows users__
```bash
python -m venv venv
venv\Scripts\activate
```

### Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Django development server:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Access the application in your web browser at http://127.0.0.1:8000.

## Features

* User Authentication:
  * Sign up
  * Log in
  * Delete account
  * Change profile information

* Post Management:
  * Create new posts
  * Update existing posts

* Comment System:
  * Authenticated users can leave comments on post detail pages.


## Project Structure

The project follows a typical Django application structure, with the following main components:

* authentication_app: Handles user authentication, including sign up, log in, profile management, and account deletion.

* blog: Manages posts and comments, including creation, updating, and deletion of posts, as well as commenting functionality.

* templates: Contains HTML templates for rendering web pages.

* static: Stores static files such as CSS, JavaScript, and images.

# Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.
