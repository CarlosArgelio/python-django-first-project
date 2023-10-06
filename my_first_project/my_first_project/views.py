from django.http import HttpResponse
from datetime import datetime


def hello(req):
    return HttpResponse("Hello World")

def bye(req):
    return HttpResponse('Bye bye')

def get_time_now(req):

    date_now = datetime.now()
    
    document_html = """
    <h1> Date and hours now is %s </h1>
    """ % date_now

    return HttpResponse(document_html)

def calc_age(req, age):
    
    age_now = 18
    period = age - 2023
    age_future = age_now-period

    document = """
    <html>
        <body>
            <h2> En el ano %s tendras %s anos </h2>
        </body>
    </html>
    """ %(age, age_future)

    return HttpResponse(document)