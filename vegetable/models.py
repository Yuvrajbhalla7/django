from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class recipe(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE, null = True ,blank = True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    image = models.ImageField(upload_to="imgrecipe")
    recipe_vcount = models.IntegerField(default=1)


class Department(models.Model):
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.department

    class Meta:
        ordering = ["department"]


class studentID(models.Model):
    student_id = models.CharField(max_length=50)

    def __str__(self):
        return self.student_id

class student(models.Model):
    department = models.ForeignKey(Department,related_name="student_id",on_delete=models.CASCADE)
    student_id = models.OneToOneField(studentID, related_name ="studentid",on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(unique=True)
    age = models.IntegerField(default =18)
    student_address = models.TextField()

    def __str__(self):
        return self.student_name

    class Meta:
        ordering=["student_name"]
        verbose_name = "student"







 

 