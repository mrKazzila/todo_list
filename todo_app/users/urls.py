from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import (UserLoginView, UserLogoutView, UserProfileUpdateView,
                         UserRegistrationCreateView)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserRegistrationCreateView.as_view(), name='signup'),
    path('profile/<int:pk>', login_required(UserProfileUpdateView.as_view()), name='profile'),
    path('logout/', login_required(UserLogoutView.as_view()), name='logout'),
]
