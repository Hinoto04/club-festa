from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User as djangoUser
from core.models import TimeStampedModel
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class User(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    year = models.IntegerField(default=2021)
    number = models.IntegerField()
    regi_date = models.DateField(auto_created=True)
    django_user = models.ForeignKey(djangoUser, on_delete=CASCADE)
    email = models.EmailField()
    profile_message = models.CharField(max_length=200, default=' ')
    interested_in = models.CharField(max_length=20, default=' ')
    description = models.TextField(default=' ')
    lastedit = models.DateField(auto_now=True, auto_now_add=False)
    like = models.TextField(default='/')
    noticelike = models.TextField(default='/')

    def __str__(self):
        if self.type == 'Student':
            return str(self.number) + " " + self.name
        else:
            return self.name

class UserLoginLog(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        related_name='login_logs',
        blank=True,
        null=True,
        on_delete=CASCADE
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP Address')
    )
    user_agent = models.CharField(
        verbose_name=_('HTTP User Agent'),
        max_length=300
    )
    
    class Meta:
        verbose_name = _('user login log')
        verbose_name_plural = _('user login logs')
        ordering = ('-created', )
        
    def __str__(self):
        return '%s %s' % (self.user, self.ip_address)