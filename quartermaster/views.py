from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django import http
from django.views.decorators.cache import cache_control
from django.views.decorators.http import etag
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.csrf import csrf_protect
#from django.db.models import F # used in Download view
from django.template import RequestContext, loader
from os import environ
# Create your views here.

def admin_view(request):
    "Handles the admin control panel."

    template_vars = {
            'number_of_users': 0
            }

    return render_to_response('admin.html', template_vars, context_instance=RequestContext(request))
