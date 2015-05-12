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

    orgs = {}
    misc = {}

    # Codecademy
    org = "Codecademy"
    orgs[org] = []

    title = 'Python'
    description = "Learn to program in Python, a powerful language used by sites like YouTube and Dropbox."
    url = "http://www.codecademy.com/en/tracks/python"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    title = 'HTML & CSS'
    description = "Learn how to create websites by structuring and styling your pages with HTML and CSS."
    url = "http://www.codecademy.com/en/tracks/web"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    title = 'jQuery'
    description = "Learn how to make your websites interactive and create animations by using jQuery."
    url = "http://www.codecademy.com/en/tracks/jquery"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    title = 'JavaScript'
    description = "Learn the fundamentals of JavaScript, the programming language of the Web."
    url = "http://www.codecademy.com/en/tracks/javascript"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    # edX
    org = "edX"
    orgs[org] = []

    title = 'MITx: 6.00.1x Introduction to Computer Science and Programming'
    description = "6.00.1x is an introduction to computer science as a tool to solve real-world analytical problems."
    url = "https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-0"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    title = 'MITx: 6.00.2x Introduction to Computational Thinking and Data Science'
    description = "6.00.2x is an introduction to using computation to understand real-world phenomena."
    url = "https://www.edx.org/course/introduction-computational-thinking-data-mitx-6-00-2x-0"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    title = 'Microsoft: DEV203x Introduction to Bootstrap'
    description = "Learn how to use Bootstrap to implement mobile first web pages with CSS and JavaScript."
    url = "https://www.edx.org/course/introduction-bootstrap-tutorial-microsoft-dev203x"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    title = 'LFS101x.2 Introduction to Linux'
    description = "Develop a good working knowledge of Linux using both the graphical interface and command line, \
    covering the major Linux distribution families."
    url = "https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-2"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    title = 'NotreDameX: SOC120x I Heart Stats: Learning to Love Statistics'
    description = "By successfully completing this course, students will learn to: 1) Select appropriate statistical \
    tests for data according to the levels of measurement 2) Perform basic calculations to determine statistical \
    significance 3) Use standard methods of representation to summarize data 4) Interpret and assess the credibility \
    of basic statistics."
    url = "https://www.edx.org/course/i-heart-stats-learning-love-statistics-notredamex-soc120x#!"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    # MongoDB University
    org = "MongoDB University"
    orgs[org] = []

    title = 'MM101P: MongoDB For Python Developers'
    description = "Learn everything you need to know to get started building a MongoDB-based app. This course will go \
    over basic installation, JSON, schema design, querying, insertion of data, indexing and working with the Python \
    driver. We will also cover working in sharded and replicated environments. In the course, you will build a \
    blogging platform, backed by MongoDB. A brief Python introduction is included in the course."
    url = "https://university.mongodb.com/courses/M101P/about"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    # Udacity
    org = "Udacity"
    orgs[org] = []

    title = 'CS215: Intro to Algorithms'
    description = "By the end of this class you will understand key concepts needed to devise new algorithms for \
    graphs and other important data structures and to evaluate the efficiency of these algorithms."
    url = "https://www.udacity.com/course/intro-to-algorithms--cs215"
    python_course = add_course(title, description, url)
    orgs[org].append(title)

    # Tutorials and Guides
    org = "Tutorials and Guides"
    misc[org] = []

    title = 'Building Web Applications with Django and AngularJS'
    description = """Each tutorial we release has a specific goal. In this tutorial, that goal is to give you a brief \
    overview of how Django and AngularJS play together and how these technologies can be combined to build amazing web \
    applications. Furthermore, we place a heavy emphasis on building good engineering habits. This includes everything \
    from considering the tradeoffs that come from making architectural decisions, to maintaining high quality code \
    throughout your project. While these things may not sound like fun, they are key to becoming a well-rounded \
    software developer."""
    url = "https://thinkster.io/django-angularjs-tutorial/"
    python_course = add_course(title, description, url)
    misc[org].append(title)

    title = 'Build a Reddit Bot'
    description = "Build a simple Reddit Bot that will monitor and reply to posts and comments."
    url = "http://pythonforengineers.com/build-a-reddit-bot-part-1/"
    python_course = add_course(title, description, url)
    misc[org].append(title)

    title = 'Web Scraping With Scrapy and MongoDB'
    description = "In this article we’re going to build a scraper for an actual freelance gig where the client wants a \
    Python program to scrape data from Stack Overflow to grab new questions (question title and URL). Scraped data \
    should then be stored in MongoDB. It’s worth noting that Stack Overflow has an API, which can be used to access \
    the exact same data. However, the client wanted a scraper, so a scraper is what he got."
    url = "https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/"
    python_course = add_course(title, description, url)
    misc[org].append(title)

    title = 'Recreating the “Building a Blog in Django” Screencast'
    description = "Build a fully functional blog using Django 1.7. Includes Syntax changes in Python 3.4, QuerySets \
    and Custom Managers, Admin and ModelAdmin, Rich-text posts with django-markdown, Generic Class-based Views, Tags, \
    RSS Feeds, Migrations, and Running testcases."
    url = "http://arunrocks.com/recreating-the-building-a-blog-in-django-screencast/"
    python_course = add_course(title, description, url)
    misc[org].append(title)

    # Miscellaneous
    org = "Miscellaneous"
    misc[org] = []

    title = 'CS183B: How to Start a Startup'
    description = "Everything we know about how to start a startup, for free, from some of the world experts. CS183B \
    is a class we taught at Stanford. It’s a sort of one-class business course for people who want to start startups."
    url = "http://startupclass.samaltman.com/lists/about"
    python_course = add_course(title, description, url)
    misc[org].append(title)

    title = 'CheckiO'
    description = "CheckiO is the game for coders. Improve your code with the help of our community. Create missions \
    and challenge your peers."
    url = "http://www.checkio.org/user/DJO3/"
    python_course = add_course(title, description, url)
    misc[org].append(title)

    for org in orgs.keys():
        add_org(org, True, slugify(org))
        o = EduOrg.orgs.get(title=org)
        for course in orgs[org]:
            c = Course.objects.get(title=course)
            o.courses.add(c)

    for org in misc.keys():
        add_org(org, False, slugify(org))
        o = EduOrg.orgs.get(title=org)
        for course in misc[org]:
            c = Course.objects.get(title=course)
            o.courses.add(c)


    # Print out Courses and Organizations
    for c in Course.objects.all():
        print("Found Course {0}".format(str(c)))

    for o in EduOrg.orgs.all():
        print("Found Organization {0}".format(str(o)))

# Start execution here!
if __name__ == '__main__':
    print("Starting Course and Organization population script...")
    populate()