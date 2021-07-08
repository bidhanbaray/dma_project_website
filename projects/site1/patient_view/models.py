from django.db import models

class patient_key(models.Model):
    patient_id = models.CharField(max_length = 200) #same as device_id,user
    approval_key = models.CharField(max_length = 200) # recquired by doctors


    def __str__(self):
        return self.patient_id