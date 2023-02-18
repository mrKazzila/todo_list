from django.shortcuts import render


def signup_user(requesr):
    return render(request=requesr, template_name='todo/signup.html', content_type={})
