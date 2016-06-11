from django.contrib import auth
import pytz
from eq import settings
from datetime import datetime, timedelta


def forced_login(request, user, remember_me=None):
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)
    enforce_remember_me(request, remember_me)


def enforce_remember_me(request, remember_me):
    if not remember_me:
        request.session.set_expiry(0)
    else:
        request.session.set_expiry(datetime.now(pytz.utc) + timedelta(days=settings.AUTH_SESSION_TIMEOUT_DAYS))
