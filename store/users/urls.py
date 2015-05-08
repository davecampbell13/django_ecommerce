from django.conf.urls import url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/signup/$', views.signup, name='signup'),
    url(r'^/register/$', views.register, name='register'),
    url(r'^/log_in/$', views.log_in, name='log_in'),
    url(r'^/login_user/$', views.login_user, name='login_user'),
    url(r'^/profile/$', views.profile, name='profile'),
    url(r'^/logout/$', views.logoutnow, name='logoutnow'),


    

]
