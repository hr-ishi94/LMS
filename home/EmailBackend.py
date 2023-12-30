from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self,email=None,password=None):
        Usermodel=get_user_model()

        try:
            user=Usermodel.objects.get(email=email)
        except Usermodel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None