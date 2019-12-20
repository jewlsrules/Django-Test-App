from django.http import HttpResponse
from django.shortcuts import render


def do_calculation(value1, value2):
    return value1 * value2

def test_function(request):
    total = do_calculation(10, 2)
    p_flag = False
    people = ['John', 'Cindy', 'Fred', 'Kelsey', 'Kami', 'Charlotte']
    return render(request, 'example.html', {'total': total, 'people': people, 'p_flag': p_flag} )

def list_clients(request):
    return HttpResponse('Hello World')

def special_case_2003(request):
    return HttpResponse('Special Cases for 2003')

def special_case(request, year):
    return HttpResponse('::Returning articles from %s' % year)

def month_archive(request, year, month):
    return HttpResponse('::Returning articles from %s and month %s' % (year, month))

def hello(request, name):
    return HttpResponse('Hello %s ' % name)