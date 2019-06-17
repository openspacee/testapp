from django.http import HttpResponse


def health(req):
    return HttpResponse('<b>ok</b><br/>I\'m fine\n')
