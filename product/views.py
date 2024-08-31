# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import User
from .forms import UserEntry

def show_product(request):
    all_product = Product.objects.all
    return render(request, "product/show_product.html", {'my_products':all_product})


def login(request):
    if request.method == "POST":
        email_input = request.POST.get("email")
        password_input = request.POST.get("password")
        user = User.objects.get(email = email_input)
        if user.password == password_input:
            # return HttpResponse(f"You are Logged in {user.fname} {user.lname} password {user.password}")
            return render(request, "product/homepage.html", {})
        else:
            return HttpResponse("Wrong Password")
    else:
        return render(request, "product/login_page.html", {})


def signup(request):
    if request.method == "POST":
        form = UserEntry(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "product/login_page.html", {})
    else:
        return render(request, "product/signup_page.html", {})
    
    # def logout(request)
    #     return redirect('home')  # Redirect to home or login page