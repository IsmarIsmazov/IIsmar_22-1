from django.shortcuts import render, HttpResponse, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from users.utils import get_user_from_request
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView, TemplateView, RedirectView





class LoginView(TemplateView, ):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        return {
            'form': LoginForm,
            'user': get_user_from_request(self.request)
        }

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/posts')
            else:
                form.add_error("username", "Bad request")
        data = {
            "form": form
        }
        return render(request, 'users/login.html', context=data)




class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/posts/')



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        return {
            'form': self.form_class,
            'user': get_user_from_request(self.request)
        }

    def post(self, request, *args, **kwargs):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                login(request, user)
                return redirect('/posts')
            else:
                form.add_error('password1', 'Password do not match')
        data = {
            'form': form,
            'user': get_user_from_request(request)
        }
        return render(request, 'users/register.html', context=data)