from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [

    url(r'^$', views.index),
    url(r'^result$', views.show),
    url(r'^survey/process$', views.process),
    url(r'^survey/reset$', views.reset),

]
