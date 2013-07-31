from django.conf.urls.defaults import *

# On the deployed version, homedir will always be ''
import os
homedir = os.path.abspath(os.path.dirname(__file__))

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    # Django "warmup" request for appengine, don't touch this
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),

    # Main pages
    ('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    
    ('^overview$', 'app.views.overview', {}),
    ('^stats$', 'app.views.stats', {}),
    
    # Static files OLD DECLARATIONS FROM ANOTHER PROJECT - NOT PART OF QUARTERMASTER - EXAMPLES ONLY
    #('^favicon.ico$', 'django.views.generic.simple.redirect_to',
        #{'url': 'http://s3.mediasnak.com/assets/favicon.ico', 'permanent' : True}),
    #('^icon.png$', 'django.views.generic.simple.redirect_to',
        #{'url': 'http://s3.mediasnak.com/assets/icon.png', 'permanent' : True}),

    # Below not needed - path overridden in app.yaml
    #('^robots.txt$', 'django.views.static.serve',
    # {'path': 'quartermaster/static/robots.txt', 'document_root' : homedir}),
    #('^static/style.css$', 'django.views.static.serve',
    # {'path': 'app/static/style.css', 'document_root' : homedir}),
    #('^static/logo.png$', 'django.views.static.serve',
    # {'path': 'app/static/logo.png', 'document_root' : homedir}),
)