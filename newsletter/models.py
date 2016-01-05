from django.db import models


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(default='', blank=True, null=True, max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s with %s' % (self.full_name, self.email)
