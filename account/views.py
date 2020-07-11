from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, ImageForm
from django.db import IntegrityError
from .models import Account


def registration_view(request):
    context = {}
    if request.method == 'GET':
        form = RegistrationForm()
        context['registration_form'] = form
        return render(request, 'account/register.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            phn = request.POST['phone_no'].replace(" ", "")
            try:
                user = Account.objects.create_user(request.POST['email'],
                                                password=request.POST['password1'],
                                                username=request.POST['username'],
                                                gender=request.POST['gender'],
                                                phone_no=phn,
                                                prof_img=None)
                user.save()
                login(request, user)
                return redirect('account:image')
            except IntegrityError:
                return render(request, 'account/register.html', {'form':RegistrationForm()})
        else:
            return render(request, 'account/register.html', {'form':RegistrationForm()})


def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


def image_view(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    context = {}
    if request.POST:
        form = ImageForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = ImageForm()
        context['account_form'] = form
        return render(request, "account/image.html", context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.initial = {
            "email": request.POST['email'],
            "username": request.POST['username'],
            "gender": request.POST['gender'],
            "phone_no": request.POST['phone_no'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
            initial={
            "email": request.user.email,
            "username": request.user.username,
            "gender": request.user.gender,
            "phone_no": request.user.phone_no,
            "prof_img": request.user.prof_img,
            })

    context['account_form'] = form
    return render(request, "account/account.html", context)
