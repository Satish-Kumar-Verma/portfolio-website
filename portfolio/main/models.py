from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('collaborator', 'Collaborator'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users' 


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.TextField(null=True, blank=True)  # Optional
    image = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    github = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'projects' 


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null=True, blank=True)
    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    ]
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='Intermediate')

    class Meta:
        db_table = 'skills' 


class ContactMessage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact_messages' 



class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, null=True, blank=True)
    testimonial = models.TextField()
    image = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'testimonials'  
