from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer, ChangePasswordSerializer
from django.contrib.auth import login, authenticate, logout
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
#import jwt.datetime
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .forms import NewUserForm


def Home(request):

    return render(request=request, template_name="employee_register/Home.html",)
def test(request):

    return render(request=request, template_name="employee_register/test.html",)

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })



class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("employee_register:base")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="employee_register/register.html", context={"register_form":form})


def login_request(request):
        if request.method == "POST":
            print("aasdfghjklllll",request)
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                print("#################trst")
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                print(username,password)
                user = authenticate(username=username, password=password)
                print("sdfghjkl;;;;;;;kjhggggggghjk",user)

                if user is not None:
                    print("12345",user)
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect('test')
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()
        return render(request=request, template_name="employee_register/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login_request")