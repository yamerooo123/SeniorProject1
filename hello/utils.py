from django.contrib.auth.models import User

def delete_users():
    User.objects.filter(password='12345').delete()