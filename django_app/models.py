from django.db import models

# Create your models here.
class Student(models.Model):
  name=models.CharField(max_length=100)
  roll_no=models.IntegerField(unique=True)
  age=models.IntegerField()
  contact=models.CharField(max_length=100,unique=True)
  def _str_(self):
      return str(self.roll_no)+" - "+self.name
class Marks(models.Model):
   student=models.ForeignKey(Student,on_delete=models.CASCADE)
   Telugu=models.IntegerField()
   Hindi=models.IntegerField()
   English=models.IntegerField()
   Science=models.IntegerField()
   def _str_(self):
       return self.student.name+" - Marks"