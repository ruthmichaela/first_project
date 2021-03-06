from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import (TemplateView, RedirectView,)
from collection import views
from collection.backends import MyRegistrationView



urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
	url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
	#things
	url(r'^things/$', RedirectView.as_view(pattern_name='browse', permanent=True)),
	url(r'^things/(?P<slug>[-\w]+)/$', views.thing_detail, name='thing_detail'),
	url(r'^things/(?P<slug>[-\w]+)/edit/$', views.edit_thing, name='edit_thing'),
	url(r'^browse/name/$', views.browse_by_name, name='browse'),
	url(r'^browse/name/(?P<initial>[-\w]+)/$', views.browse_by_name, name='browse_by_name'),
	#acounts
	url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
	url(r'^accounts/create_thing/$', views.create_thing, name='registration_create_thing'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^admin/', admin.site.urls),
]
