from django.urls import path
from django.contrib import admin
from .views import home_view
from authentication.views import login_view
# from authentication.views import signup_with_email_verification, home, account_activation_sent
# from authentication import forms
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', home_view),
    path(r'login/', login_view, name='login_url'),
    # path(r'^register/', signup_with_email_verification, name='register'),
    # path(r'^home/$', home, name='home'),
    # path(r'^login/$', auth_views.login,{'template_name':'login.html','authentication_form':forms.LoginForm}, name='login'),
    # path(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    # path(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    # path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #                      views.activate, name='activate'),
]