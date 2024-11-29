from django.shortcuts import render, redirect
from home.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        # Handle Signup
        if "username" in request.POST :
            username = request.POST.get('username')
            email = request.POST.get('signup_email')
            password = request.POST.get('signup_p')

            if not username or not email or not password:
                messages.warning(request, "Enter all fields!")
                return redirect('/login_view')

            if CustomUser.objects.filter(username=username).exists():
                messages.warning(request, "Username already exists, try a new one!")
                return redirect('/login_view')

            user = CustomUser(username=username, email=email)
            user.set_password(password)  # Hash the password
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('https://tranquil-otter-dd17ea.netlify.app/')

        # Handle Login
        else:
            email = request.POST.get('email')
            password = request.POST.get('password')

            if not email or not password:
                messages.warning(request, "Oops! Looks like some fields are missing. Try again.")
                return render(request, 'login.html')

            user = authenticate(request, email=email, password=password)  # Pass request to authenticate
            if user is not None:
                login(request, user)
                return redirect('https://tranquil-otter-dd17ea.netlify.app/')
            else:
                messages.error(request, "Bad Credentials!")
                return render(request, 'login.html')

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('/')
