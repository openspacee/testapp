from django.http import HttpResponse


def health(req):
    return HttpResponse('<b>111ok</b><br/>I\'m fine\n')
