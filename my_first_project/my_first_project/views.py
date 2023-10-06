from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

route_base = "/home/carlos/work/projects/python/frameworks/django/course_1"

def hello(req):

    home_html = route_base + "/my_first_project/my_first_project/templates/home.html"
    document = open(home_html)

    plt = Template(document.read())

    document.close()

    ctx = Context()

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