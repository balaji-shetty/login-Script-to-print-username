import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "login.settings")
django.setup()

from django.contrib.auth import authenticate, login

def perform_login(username, password):
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            #login(user)
            print("Login successful.")
            print("Username:", user.username)
        else:
            print("This user account is inactive.")
    else:
        print("Login failed. Invalid username or password.")

# Usage example:
username = input("Enter your username: ")
password = input("Enter your password: ")
perform_login(username, password)
