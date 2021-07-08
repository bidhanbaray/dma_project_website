from django.db import models

class doctor_data(models.Model):
    doctor_id = models.CharField(max_length = 200)
    patient_id = models.CharField(max_length = 200)


    def __str__(self):
        return self.doctor_id