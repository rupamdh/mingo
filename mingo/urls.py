from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin-logout/', logout_view, name='admin-logout'),

]
