from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import auth
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from .models import User
# Create your views here.


def registration(request):
    user_form = UserRegistrationForm()
    template_name = 'account/register.html'
    context = {'user_form': user_form}
    if request.method == "POST":
        data = request.POST
        email = data['email']   # str
        password1 = data['password']   # str
        password2 = data['password2']   # str
        user = User.objects.filter(email=email)
        if user.exists():
            messages.info(request, "This '{}' email already exists".format(email))
            return redirect("register")
        if password1 and password2 and password1 != password2:
            messages.info(request, "Passwords don't match")
            return redirect("register")
        else:
            user = User.objects.create_user(email=email, password=password2)
            user.save()
            messages.success(request, f"Account created for {email}!")
            return redirect("login")
    else:
        return render(request, template_name=template_name, context=context)


def login(request):
    user_form = UserLoginForm()
    template_name = 'account/register.html'
    context = {'user_form': user_form}
    if request.method == "POST":
        data = request.POST
        email = data['email']   # str
        password = data['password']   # str
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Success credentials")
            return redirect("list")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, template_name=template_name, context=context)


def user_list(request):
    template_name = 'account/user-list.html'
    users = User.objects.all()
    context = {"users": users}
    return render(request, template_name=template_name, context=context)


@login_required
def profile_edit(request):
    user = request.user
    form = UserProfileForm(request.POST or None, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            user.userprofile.first_name = request.POST['first_name']
            user.userprofile.last_name = request.POST['last_name']
            user.userprofile.country = request.POST['country']
            user.userprofile.city = request.POST['city']
            user.userprofile.phone = request.POST['phone']
            user.save()
            return redirect("list")
    context = {
        "user_form": form
    }
    return render(request, 'account/update.html', context)