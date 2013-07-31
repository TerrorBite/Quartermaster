from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django import http
from django.views.decorators.cache import cache_control
from django.views.decorators.http import etag
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.csrf import csrf_protect
#from django.db.models import F # used in Download view
from django.template import RequestContext, loader
from django.core.exceptions import PermissionDenied
from django.http import Http404
from os import environ
# Create your views here.

import user

def admin_view(request):
    "Handles the admin control panel."

    template_vars = {
            'user_list': [] #example
            }

    return render_to_response('admin.html', template_vars, context_instance=RequestContext(request))

def stats_view(request):
    "Generates/retrieves statistics to be presented to the user."

    template_vars = {
            # Just examples for now
            'number_of_users': 0,
            'active_users_in_last_week': 0,
            'total_resonators': 0,
            'total_xmps': 0,
            }

    return render_to_response('stats.html', template_vars, context_instance=RequestContext(request))

def confirmlogin_view(request):
    "Handles user logins, checking if a user is new to the system."

    # Check if we do, in fact, have a logged-in user right now
    if not user.is_logged_in():
        raise PermissionDenied # respond with 403 page

    to = request.REQUEST['returnto']
    if not to.startswith('/'): to = '/'

    return redirect(to, False)
