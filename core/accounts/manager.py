from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    '''Custom User Account Creation Manager'''

    def create_user(self, username, password, **kwargs):
        user = self.model(username=username, password=password, **kwargs)  # noqa
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **kwargs):
        user = self.create_user(username=username, password=password, **kwargs)  # noqa
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
