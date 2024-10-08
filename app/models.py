from django.db import models
import uuid

class User(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(blank=True, null=True, max_length=300, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    otherNames = models.CharField(blank=True, null=True, max_length=80)
    surname = models.CharField(blank=True, null=True, max_length=80)
    level = models.CharField(blank=True, null=True, max_length=80)
    matricNumber = models.CharField(blank=True, null=True, max_length=30)
    dateOfBirth = models.DateField()
    gender = models.CharField(blank=True, null=True, max_length=15)
    studentPhoneNumber = models.CharField(blank=True, null=True, max_length=15)
    # maritalStatus = models.CharField(blank=True, null=True, max_length=30)
    # nationality = models.CharField(blank=True, null=True, max_length=110)
    # stateOfOrigin = models.CharField(blank=True, null=True, max_length=110)
    # localGovtArea = models.CharField(blank=True, null=True, max_length=110)
    
    # passport = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.surname
    
    def get_registered_courses(self):
        return self.registration_set.all()
    
class Level(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=80)
    
    def __str__(self):
        return self.name
    
class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=500)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Programme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=500)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=True, null=True, max_length=500)
    courseCode = models.CharField(blank=True, null=True, max_length=15)
    # courseDescription = models.CharField(blank=True, null=True, max_length=250)
    unit = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    programmes = models.ManyToManyField(Programme, related_name='courses')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.courseCode} - {self.title}"

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=500)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phoneNumber = models.CharField(blank=True, null=True, max_length=15)

    def __str__(self):
        return self.name

class Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    registration_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(blank = True, null=True)
    approved_by = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date_approved = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.surname} - {self.registration_date}"
    


