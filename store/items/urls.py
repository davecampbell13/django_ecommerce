from django.conf.urls import url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/$', views.index, name='index'),
    url(r'(?P<item_id>[0-9]+)/$', views.show, name='show'),
    url(r'^/cart/', views.cart, name='cart'),
    url(r'(?P<item_id>[0-9]+)/add$', views.add, name='add'),
    url(r'(?P<item_id>[0-9]+)/delete$', views.delete, name='delete'),
    url(r'/payment/$', views.payment, name='payment'),
    url(r'/thankyou$', views.thankyou, name='thankyou'),
    ]