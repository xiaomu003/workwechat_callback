from django.urls import path,re_path

from . import views

urlpatterns = [
    re_path('cburl/(?P<msg_signature>)(?P<timestamp>)(?P<nonce>)(?P<echostr>)', views.cburl),
]