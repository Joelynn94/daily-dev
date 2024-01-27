from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from projects.models import Project
from sprints.models import Sprint
from tasks.models import Task
from dailylogs.models import DailyLog
from .forms import UserForm


def account_logout(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect("login")


def account_login(request):
    if request.user.is_authenticated:
        return redirect("dailylog_list")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try: 
            username = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist.")
            return render(request, "registration/login.html")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # creates a session for the user
            login(request, user)
            messages.success(request, "You have logged in successfully.")
            return redirect("dailylog_list")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "registration/login.html")
    return render(request, "registration/login.html")


def account_register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account created.")
            return redirect("dailylog_list")
        else:
            messages.error(request, f"An error has occurred during registration")
    else:
        form = UserForm()

    return render(request, "registration/register.html", {"form": form})


def overview(request):
    projects = Project.objects.all()
    sprints = Sprint.objects.all()
    tasks = Task.objects.all()
    dailylogs = DailyLog.objects.all()

    context = {
        "projects": projects,
        "sprints": sprints,
        "tasks": tasks,
        "dailylogs": dailylogs,
        "projects_count": projects.count(),
        "sprints_count": sprints.count(),
        "tasks_count": tasks.count(),
        "dailylogs_count": dailylogs.count(),
    }

    return render(request, "core/overview.html", context)