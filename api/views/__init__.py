from django.http import HttpResponse


def health(req):
    return HttpResponse('<b>3333</b><br/>I\'m fine\n')
