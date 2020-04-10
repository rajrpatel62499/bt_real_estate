from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from contacts.models import Contact

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # password checking
        if password1 == password2:
            # user checking in database
            if User.objects.filter(username=username).exists():
                messages.error(request, message="User already exists")
                return redirect(to="accounts-register")
            else:
                # email checking
                if User.objects.filter(email=email).exists():
                    messages.error(request, message="Email already used")
                    return redirect(to="accounts-register")
                else:
                    # Everything looks good,Now save data to database
                    """REGISTER"""
                    user = User.objects.create_user(
                        username=username,
                        password=password1,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.save()  # this will store to the database

                    """LOG IN"""
                    # after register i want to automatically logged in
                    auth.login(
                        request, user=user
                    )  # this method persist user_id throught the session
                    messages.success(
                        request, message="You are registerd and logged in!!",
                    )
                    # redirected to dashboard after logged in
                    return redirect(to="accounts-dashboard")
        else:
            messages.error(request, message="Password doesn't match")
            return redirect(to="accounts-register")
    else:
        return render(request, "accounts/register.html")


def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user=user)
            messages.success(request, message="You are logged in!")
            return redirect(to="accounts-dashboard")
        else:
            messages.error(request, message="Invalid Credentials")
            return redirect(to="accounts-login")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, message="You are logged out!")
        return redirect("pages-index")


def dashboard(request):
    user_contacts =Contact.objects.all().order_by("-contact_date").filter(user_id=request.user.id)
    context = {"contacts": user_contacts}
    return render(request, "accounts/dashboard.html", context)


def admin(request):
    return render(request, "admin/base_site.html")
