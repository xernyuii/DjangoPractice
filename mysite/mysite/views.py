from django.http import HttpResponse,Http404
import datetime
from django.template import Template, Context

#get time
def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)



def hello(request):
    return HttpResponse("Hello, world!")

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s. </body></html>" % (offset, dt)
    return HttpResponse(html)



