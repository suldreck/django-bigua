from django.conf.urls.defaults import *
from os.path import abspath, dirname

path_to_media = '%s/media' % dirname(abspath(__file__))
urlpatterns = patterns('',
    # Example:
    # (r'^soma/', include('soma.foo.urls')),
    (r'^$', 'canchas.views.index'),
    (r'^login/$', 'canchas.views.do_login'),
    (r'^logout/$', 'canchas.views.do_logout'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': path_to_media }),
    (r'^reservar/(?P<cancha>\d*)/(?P<dia>\d*)/(?P<hora>\d*)/$', 'canchas.views.reservar'),
    (r'^reservar/$', 'canchas.views.do_reservar'),
    (r'^cancelar/reserva/$', 'canchas.views.cancelar'),
    (r'^administrador/$', 'canchas.views.admin_login'),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
