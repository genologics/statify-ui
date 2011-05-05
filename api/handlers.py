import uuid
from piston.handler import BaseHandler
from piston.utils import rc
from log.models import Entry

class RegistrationHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, registration_id=None):
        return "%s" % uuid.uuid1()


class LogHandler(BaseHandler):
    allowed_methods = ('POST',)

    def create(self, request, *args, **kwargs):
        if request.POST.has_key('guid') and request.POST.has_key('key') and request.POST.has_key('value'):
            log_entry = Entry(guid=request.POST['guid'], key=request.POST['key'], value=request.POST['value'])
            log_entry.save()
            return rc.CREATED

        return rc.BAD_REQUEST
