from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    proposer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Person(models.Model):
    roll_number = models.CharField(max_length=10)

    def __str__(self):
        return self.roll_number

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person} - {self.project}"
