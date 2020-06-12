from django.urls import path
from .views import registration, login, user_list, profile_edit

urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', login, name='login'),
    path('list/', user_list, name='list'),
    path('update/', profile_edit, name='update'),
]