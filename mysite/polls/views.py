from django.http import HttpResponse


def index(request):
    s = "testing"
    print(s)
    return HttpResponse("Hello, world. You're at the polls index.")
