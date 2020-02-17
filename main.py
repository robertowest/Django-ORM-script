#!/usr/bin/env python

# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from data.models import *


def create_user():
    #Add user
    user = User(name="masnun", email="masnun@gmail.com")
    user.save()

    # Application logic
    first_user = User.objects.all()[0]

    print(first_user.name)
    print(first_user.email)


def create_publisher():
    # probamos el modelo
    p = Publisher()
    p.name = 'O REILLY'
    p.address = '898  Bell Street'
    p.city = 'New York'
    p.state_province = 'New York'
    p.country = 'EEUU'
    p.website = 'https://www.learnpython.org/es/'
    p.save


def create_author():
    a = Author()
    a.first_name = 'Mark'
    a.last_name = 'Lutz'
    a.salutation = 'Sr.'
    a.save()


def create_books(authors, publisher):
    b = Book()
    b.title = 'Learning Python: Powerful Object-Oriented Programming'
    b.authors = authors
    b.publisher = publisher
    b.publication_date = '2013-09-07'
    b.save()

    b.title = 'Python Pocket Reference: Python in Your Pocket'
    b.publication_date = '2014-02-11'
    b.save()


if __name__ == "__main__":
    create_publisher()
    # create_author()
    # create_books
