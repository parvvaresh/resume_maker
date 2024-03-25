from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Experience(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"


class Education(models.Model):
    institution_name = models.CharField(max_length=100, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.institution_name} - {self.degree}"


class Skill(models.Model):
    skill_name = models.CharField(max_length=100, null=True, blank=True)
    skill_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.skill_name


class Project(models.Model):
    project_name = models.CharField(max_length=100, null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.project_name


class Language(models.Model):
    language = models.CharField(max_length=100, null=True, blank=True)
    language_level = models.CharField(max_length=100, null=True, blank=True)
    is_native = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.language


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    work_experience = models.ManyToManyField(Experience, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    languages = models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return self.name
