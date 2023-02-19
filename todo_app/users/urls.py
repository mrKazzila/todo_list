from django.urls import path

from users.views import (UserLoginView, UserRegistrationCreateView,
                         user_logout_view)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserRegistrationCreateView.as_view(), name='signup'),
    path('logout/', user_logout_view, name='logout'),
]
