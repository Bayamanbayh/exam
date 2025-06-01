from django.db import models
from django.contrib.auth.models import AbstractUser

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('client', 'client'),
        ('freelancer', 'freelancer')
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='client')
    bio = models.CharField(max_length=24, null=True, blank=True)
    avatar = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    skill = models.ManyToManyField(Skill, null=True, blank=True)
    social_links = models.CharField(max_length=100, null=True, blank=True)

class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    budget = models.PositiveIntegerField()
    deadline = models.DateField(auto_now=False)
    Project_CHOICES = (
        ('open', 'open'),
        ('in_progress', 'int_progress'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled')
    )
    project_role = models.CharField(max_length=16, choices=Project_CHOICES, default='open')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_project')
    skills_required = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skills_project')
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_project')
    created_at = models.DateField(auto_now=True)

class Offer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='offer_project')
    freelancer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='freelancer_project')
    message = models.TextField()
    proposed_budget = models.PositiveIntegerField()
    proposed_deadline = models.DateField(auto_now=False)
    created_at = models.DateField(auto_now=True)

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='review_p')
    target = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='freelancer_review')
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='ratings')
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



