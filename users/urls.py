from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('<int:id>/follow_toggle', follow_toggle, name="follow_toggle"),
    path('profile_page/', profile_page, name="profile_page"),
    path('following_list/', following_list, name="following_list"),
    path('follower_list/', follower_list, name="follower_list"),
]