from itertools import product
from sqlite3 import IntegrityError

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product

from .forms import ProductForm
from .models import Product, Category


# Create your views here.
def base(request):
    return render(request, 'base.html')


def home(request):
    # return HttpResponse("Welcome to my django Project")
    products = Product.objects.all()  # Retrieve all products from the database
    print(products)  # Print the products to the console
    return render(request, 'home.html', {'products': products})




def signup(request):
    if request.method == 'POST':
        username = request.POST['txt_username']
        password = request.POST['txt_pass1']
        pass2 = request.POST['txt_pass2']
        email = request.POST['txt_email']
        f_name = request.POST['txt_fname']
        lname = request.POST['txt_lname']
        if username and password and pass2:
            if password != pass2:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'signup.html')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'signin.html')
            try:
                user = get_user_model().objects.create_user(username=username, password=password)
                user.first_name = f_name  # Assuming 'first_name' exists in your User model
                user.last_name = lname  # Assuming 'phone_no' exists in your User model
                user.email = email
                user.save()
                messages.success(request, 'You are successfully registered!')
                return redirect('signin')
            except IntegrityError as e:
                messages.error(request, 'Username already exists. Please choose a different one.')
                return render(request, 'signup.html')
        else:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'signup.html')
    return render(request, 'signup.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['txt_username']
        password = request.POST['txt_pass']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)

            # Debugging print statement to ensure we're hitting this point
            print(f"User '{username}' logged in successfully. Redirecting to dashboard.")

            # Redirect to the user dashboard
            return redirect('user_dashboard')  # Ensure 'user_dash' is the correct URL name
        else:
            # Invalid credentials; show an error message
            messages.error(request, "Invalid credentials")
            return redirect('signin')

    return render(request, 'signin.html')



def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.SUCCESS(request, "Successfully added new Product")
    product_form = ProductForm()
    return render(request, 'add_product.html', {'form': product_form})


def signout(request):
    logout(request)
    return render(request, 'signin.html')


def user_dashboard(request):
    products = Product.objects.all()
    return render(request,'user_home.html',{'products': products})


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
        product_form = ProductForm(instance=product)
        return render(request, 'edit_product.html', {'form': product_form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'delete_product.html', {'product': product})


