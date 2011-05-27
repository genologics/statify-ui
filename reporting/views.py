from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response(
            'reporting/index.html',
            {
            },
            mimetype="application/xhtml+xml",
            context_instance=RequestContext(request))

