from django.db import models
from accounts.models import Account
# Create your models here.
class MakeAppointment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_completed = models.BooleanField(default=False)
    is_resceduled = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name