from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from model_utils import Choices

class User(AbstractUser):
    # user_type = models.CharField(choices=USER_TYPES, default="publisher", max_length=30)
    # meta = JSONField(default=default_somemodel_dict)
    class Meta:
        db_table = "user"

# class User(AbstractUser):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(unique=True)
#     user_type = models.CharField(choices=USER_TYPES, default="publisher", max_length=30)
#     phone = models.CharField(max_length=145, blank=True)
#     meta = jsonfield.JSONField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         db_table = "user"