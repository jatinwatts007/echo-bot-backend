from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    class Meta:
        db_table = 'user_table'
        unique_together = (('username', 'email'),)


class Chat(models.Model):
    message = models.CharField(null=False, blank=False, max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'message_table'
