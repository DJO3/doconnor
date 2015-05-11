import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doconnor.settings')

import django
from django.template.defaultfilters import slugify
django.setup()

from blog.models import Course, EduOrg, EntryQuerySet


def add_course(title, description, url):
    c = Course.objects.get_or_create(title=title, description=description, url=url)[0]
    return c


def add_org(title, publish, slug):
    o = EduOrg.orgs.get_or_create(title=title, publish=publish, slug=slug)[0]
    return o


def populate():
    title = 'Python'
    description = "Learn to program in Python, a powerful language used by sites like YouTube and Dropbox."
    url = "http://www.codecademy.com/en/tracks/python"
    python_cat = add_course(title, description, url)

    title = 'HTML & CSS'
    description = "Learn how to create websites by structuring and styling your pages with HTML and CSS."
    url = "http://www.codecademy.com/en/tracks/web"
    python_cat = add_course(title, description, url)

    title = 'jQuery'
    description = "Learn how to make your websites interactive and create animations by using jQuery."
    url = "http://www.codecademy.com/en/tracks/jquery"
    python_cat = add_course(title, description, url)

    title = 'JavaScript'
    description = "Learn the fundamentals of JavaScript, the programming language of the Web."
    url = "http://www.codecademy.com/en/tracks/javascript"
    python_cat = add_course(title, description, url)

    org = "Codecademy"
    add_org(org, True, slugify(org))

    # Print out Courses and Organizations
    for c in Course.objects.all():
        print("Found Course {0}".format(str(c)))

    for o in EduOrg.orgs.all():
        print("Found Organization {0}".format(str(o)))

# Start execution here!
if __name__ == '__main__':
    print("Starting Course and Organization population script...")
    populate()