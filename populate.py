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

    # Codecademy
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

    # edX
    title = 'MITx: 6.00.1x Introduction to Computer Science and Programming'
    description = "6.00.1x is an introduction to computer science as a tool to solve real-world analytical problems."
    url = "https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-0"
    python_cat = add_course(title, description, url)

    title = 'MITx: 6.00.2x Introduction to Computational Thinking and Data Science'
    description = "6.00.2x is an introduction to using computation to understand real-world phenomena."
    url = "https://www.edx.org/course/introduction-computational-thinking-data-mitx-6-00-2x-0"
    python_cat = add_course(title, description, url)

    title = 'Microsoft: DEV203x Introduction to Bootstrap'
    description = "Learn how to use Bootstrap to implement mobile first web pages with CSS and JavaScript."
    url = "https://www.edx.org/course/introduction-bootstrap-tutorial-microsoft-dev203x"
    python_cat = add_course(title, description, url)

    title = 'LFS101x.2 Introduction to Linux'
    description = "Develop a good working knowledge of Linux using both the graphical interface and command line, \
    covering the major Linux distribution families."
    url = "https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-2"
    python_cat = add_course(title, description, url)

    orgs = ["Codecademy", "edX", "MongoDB University", "Udacity"]
    misc = ["Miscellaneous", "Tutorials and Guides"]
    for org in orgs:
        add_org(org, True, slugify(org))
    for org in misc:
        add_org(org, False, slugify(org))



    # Print out Courses and Organizations
    for c in Course.objects.all():
        print("Found Course {0}".format(str(c)))

    for o in EduOrg.orgs.all():
        print("Found Organization {0}".format(str(o)))

# Start execution here!
if __name__ == '__main__':
    print("Starting Course and Organization population script...")
    populate()