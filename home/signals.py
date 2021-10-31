import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from ipware.ip import get_ip
from models import UserLoginLog

@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    log = UserLoginLog()
    log.user = user
    log.ip_address = get_ip(request)
    log.user_agent = request.META['HTTP_USER_AGENT']
    log.save()