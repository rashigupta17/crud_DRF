from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    # creating user
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(('The Email is not set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user