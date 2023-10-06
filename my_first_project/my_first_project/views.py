from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

route_base = "/home/carlos/work/projects/python/frameworks/django/course_1"

class Person(object):

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

def hello(req):

    person = Person("Carlos", "Palacios")

    home_html = route_base + "/my_first_project/my_first_project/templates/home.html"
    document = open(home_html)

    plt = Template(document.read())

    document.close()

    my_dict = {
        "name": person.name,
        "lastName": person.last_name
    }

    ctx = Context(my_dict)

    docs = plt.render(ctx)

    return HttpResponse(docs)

def bye(req):
    return HttpResponse('Bye bye')

def get_time_now(req):

    date_now = datetime.now()
    
    document_html = """
    <h1> Date and hours now is %s </h1>
    """ % date_now

    return HttpResponse(document_html)

def calc_age(req, age, birth):
    
    period = age - 2023
    birth_future = age-period

    document = """
    <html>
        <body>
            <h2> En el ano %s tendras %s anos </h2>
        </body>
    </html>
    """ %(birth, birth_future)

    return HttpResponse(document)