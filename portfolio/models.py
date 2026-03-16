from django.db import models

class About(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    bio = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    cv_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)
    percentage = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=255, help_text="Comma separated e.g. React, Django")
    demo_link = models.URLField(blank=True, null=True)
    repo_link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    start_date = models.CharField(max_length=50) # like 'Jan 2020'
    end_date = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. Present or Dec 2021")
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
