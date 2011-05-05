from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api.handlers import RegistrationHandler, LogHandler

class CsrfExemptResource(Resource):
    """A Custom Resource that is csrf exempt"""
    def __init__(self, handler, authentication=None):
        super(CsrfExemptResource, self).__init__(handler, authentication)
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)

registration_handler = Resource(RegistrationHandler)
log_handler = CsrfExemptResource(LogHandler)

urlpatterns = patterns('',
                       url(r'^register', registration_handler, {'emitter_format': 'text'}),
                       url(r'^log', log_handler, {'emitter_format': 'text'})
)