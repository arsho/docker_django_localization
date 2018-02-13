from django.conf import settings
from django.utils import translation


class DomainLocalMiddleware(object):
    """
    Set site language based on the domain
    """
    def process_request(self, request):
        if request.META.has_key('HTTP_ACCEPT_LANGUAGE'):
            del request.META['HTTP_ACCEPT_LANGUAGE']
        current_domain = request.META['HTTP_HOST']
        language_code = settings.LANGUAGE_DOMAINS.get(current_domain)
        if language_code:
            translation.activate(language_code)
            request.LANGUAGE_CODE = language_code

