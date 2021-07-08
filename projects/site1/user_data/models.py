from django.db import models

class user_data(models.Model):
    device_id = models.CharField(max_length = 200)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    temp = models.FloatField(default=0.00)
    bp_systolic = models.IntegerField()
    bp_diastolic = models.IntegerField()
    hr = models.IntegerField()
    spo2 = models.IntegerField()


    def __str__(self):
        return self.device_id



