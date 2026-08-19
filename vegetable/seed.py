from faker import Faker
fake = Faker()
import random
from .models import *



def seed_db(n=10)->None:
    try:
        for i in range(0,n):
            department_obj = Department.objects.all()
            random_index = random.randint(0,len(department_obj)-1)
            department=department_obj[random_index]


            student_id = f"STU-0{random.randint(100,999)}"

            student_name = fake.name()
            email = fake.email()
            age = random.randint(18,28)
            student_address = fake.address()


            student_id_obj = studentID.objects.create(
                student_id = student_id)

            
            student_obj = student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = email,
                age = age,
                student_address = student_address,

            )

    except Exception as e:
        print(e)

