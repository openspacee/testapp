from django.http import HttpResponse


def health(req):
    return HttpResponse('ok')
