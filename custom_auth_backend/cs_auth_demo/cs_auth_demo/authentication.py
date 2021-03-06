from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

#https://stackoverflow.com/questions/37332190/django-login-with-email
#https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#other-authentication-sources
#AUTHENTICATION_BACKENDS = ['path.to.auth.module.EmailBackend']
