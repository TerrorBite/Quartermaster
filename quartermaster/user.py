from google.appengine.api import users
from djangoappengine.utils import on_production_server

def get_user_nickname():
    user = users.get_current_user()
    if user:
        return user.nickname()
    else:
        return None

def is_logged_in():
    if users.get_current_user(): return True
    return False

def template_vars(request):
    """
    A context processor.
    
    Returns variables required for the base template to display login/logout links.
    """
    user = users.get_current_user()
    if user:
        return {'username': user.nickname(), 'logout_url': users.create_logout_url('/'),
            'local_logout_url': ('/_ah/logout?continue=http://%s/' % (request.get_host(),)) if on_production_server
                else ('/_ah/login?continue=http://%s/&action=Logout' % (request.get_host(),))}
    else:
        return {'login_url': users.create_login_url('/')}

def get_user_id():
    user = users.get_current_user()
    if user:
        uid = user.user_id() # string value
        return int(uid[:15]) ^ int(uid[-15:]) # 64-bit int
    else:
        return None
