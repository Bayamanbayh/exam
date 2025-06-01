from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='profile_list')
router.register(r'skill', SkillViewSet, basename='skill_list')
router.register(r'category', CategoryViewSet, basename='category_list')
router.register(r'project', ProjectViewSet, basename='project_list')
router.register(r'offer', OfferViewSet, basename='offer_list')
router.register(r'review', ReviewViewset, basename='review_list')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
