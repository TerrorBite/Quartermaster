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
        return {
                # This is the user's friendly name
                'username': user.nickname(),
                
                # This is the AppEngine-generated logout URL. However, this URL will log the user completely
                # out of their Google Account, which is probably not what they were expecting.
                'logout_url': users.create_logout_url('/'),

                # So, we create our own local logout URL that only logs them out of Quartermaster.
                'local_logout_url': ('/_ah/logout?continue=http://%s/' % (request.get_host(),)) if on_production_server

                # The AppEngine SDK test server expects a different form of logout URL, so
                # if we're not on a production server, use this one instead.
                else ('/_ah/login?continue=http://%s/&action=Logout' % (request.get_host(),))}
    else:
        return {'login_url': users.create_login_url('/confirmlogin?returnto={0}'.format(request.path))}

def get_user_id():
    """
    DEPRECATED. Retrieves a transformed form of the user's unique ID as a 64-bit integer.
    
    Google gives us the user's unique ID as a string containing a long numeric value.
    The number is too large to fit into an integer field on its own, so we mash it up a bit until it fits.
    """
    user = users.get_current_user()
    if user:
        uid = user.user_id() # string value
        return int(uid[:15]) ^ int(uid[-15:]) # 64-bit int
    else:
        return None

def get_user_id_string():
    return users.get_current_user().user_id()
