from ..Controller import *       # Base Controller



class AuthController(Controller):

    def __init__(self):
        pass


    # Login Client;
    def login(self,request):
        return render(request, 'web/auth/login.html')


    # Register Client;
    def register(self,request):
        return render(request, 'web/auth/register.html')


    # Forget Client Password;
    def forget(self,request):
        return render(request, 'web/auth/forget.html')

