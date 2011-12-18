#this is the root views.py that allows you to define 404 page errors
from django.shortcuts import render_to_response
from django.template import RequestContext

def file_not_found_404(request):
    page_title = 'Page not found'
    return render_to_response('404.html',locals(),context_instance=RequestContext(request))
