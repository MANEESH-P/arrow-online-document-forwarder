from django.conf.urls import url

from .import views
from django.contrib.auth.views import login
app_name="forwarder"
urlpatterns = [
        url(r'^$' , views.index, name='index'),
        url(r'^login/$',login,{'template_name':'forwarder/login.html'}, name="login" ),
        url(r'^staff/$',views.staff),
        url(r'^apply/$',views.apply),
        url(r'^detail/$',views.detail, name="detail"),
]
