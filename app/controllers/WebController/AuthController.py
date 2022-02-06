#------------------------------------------------------#
# AUTH CONTROLLER
#------------------------------------------------------#

from re import match
from ..Controller import *       # Base Controller
from app.models.Customer import Customer
from django.contrib.auth.models import User


class AuthController(Controller):

    def __init__(self):
        pass


    # Login Client;
    def login(self,request):
        return render(request, 'web/views/auth/login.html')


    # Logout Client;
    def logout(self,request):
        return HttpResponse("Logout...")


    # Register Client;
    def register(self,request):
        if request.method == 'POST':
            customer = Customer()
            # Checkpoint for null field;
            if not(request.POST['name'] or request.POST['email'] or request.POST['password']):
                messages.error(request, "All Fields Required (Except Username)")
                return redirect('auth.register')
            
            # Checkpoint for 'name'
            if request.POST['name']:
                temp = request.POST['name']
                # Check length of 'name';
                if len(temp) < 2:               
                    messages.error(request, "Field 'name' should be greater than 2")
                    return redirect('auth.register')

            # Checkpoint for 'email';
            if request.POST['email']:
                temp = request.POST['email']
                # for in-between space
                # for email syntax
                emailExist = Customer.objects.filter(email=temp).exists()
                if emailExist:
                    messages.error(request, f"Email '{temp}' already registered. Try Login or Forgot Password")
                    return redirect('auth.register')

            # Checkpoint for 'username';
            if request.POST['username']:
                temp = request.POST['username']
                # first word can't be number;
                # len should be greater than 2'
                # space not includes;
                # special chars not includes except (-,_) 
                # messages.error(request, "")
                # return redirect('auth.register')
                usernameExist = Customer.objects.filter(username=temp).exists()
                if usernameExist:
                    messages.error(request, f"Username '{temp}' already taken")
                    return redirect('auth.register')

            # Check for Password;
            if request.POST['password']:
                temp = request.POST['password']
                # Check for confirm password;
                if request.POST['password'] != request.POST['confirmPassword']:
                    messages.error(request, "Confirm Password not same")
                    return redirect('auth.register')
                # Check for password length;
                # if len(temp) < 8:
                #     messages.error(request, "Password must greater than or equal to 8")
                #     return redirect('auth.register')

            customer.name = request.POST['name']                        # Store 'name'
            customer.email = request.POST['email']                      # Store 'email'
            customer.username = request.POST['username']                # Store 'customername'
            customer.password = request.POST['password']                # Store 'password'

            if customer.save() != None:                                 # return 'None' if Success
                messages.error(request, 'Something Went Wrong, while updating database')
                return redirect('auth.register')

            messages.success(request, 'Customer Registered')
            return redirect('auth.register')
        else:
            return render(request, 'web/views/auth/register.html')


    # Forget Client Password;
    def forget(self,request):
        return render(request, 'web/views/auth/forget.html')


    # Reset Password;
    def resetPassword(self, request):
        return HttpResponse("Reset Password, Here...")
        # return render(request, '/../')


    # Dashboard;
    def dashboard(self, request):
        return render(request, '/web/views/dashboard.html')


