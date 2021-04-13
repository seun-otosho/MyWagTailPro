from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password):  # date_of_birth=None,
        """
        Creates and saves a User with the given email, date of birth and password.
        """
        # if not email:
        #     raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(
            email), username=username, )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):  # date_of_birth,
        """
        Creates and saves a superuser with the given email, date of birth and password.
        """
        user = self.create_user(email, username, password=password, )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
