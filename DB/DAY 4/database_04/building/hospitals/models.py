from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f"{self.name} 전문의"
    
class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 외래키 삭제함
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
    def __str__(self):
        return f"{self.pk}번 환자 {self.name}"
    
# # 중개모델 -> MtoM 하려고 주석처리함
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    
# through 용 클래스
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'