from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    # / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
    url(r'^$', views.index),

    url(r'^new$', views.new),
    # / new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.

    url(r'^create$', views.create),
    # / create - Have this be handled by a method named 'create'.  For now, have this url redirect to / .

    url(r'^(?P<number>\d+)$', views.show),
    # / {{number}} - display 'placeholder to display blog {{number}}'.  For example / 15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.

    url(r'^(?P<number>\d+)/edit$', views.edit),
    # / {{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.

    url(r'^(?P<number>\d+)/delete$', views.destroy),
    # / {{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to / .
]
