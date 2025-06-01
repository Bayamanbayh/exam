from django_filters import FilterSet
from .models import *


class ProjectFilter(FilterSet):
    class Meta:
        model = Project
        fields = {
            'title': ['exact'],
            'category': ['exact'],
            'budget': ['gt', 'lt'],
            'skills_required': ['exact'],
        }
