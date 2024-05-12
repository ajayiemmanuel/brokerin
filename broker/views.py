from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *

from .decorators import unauthenticated_user, allowed_users, admin_only



# Create your views here.

def index(request):
    context = {}
    return render (request, "broker/index.html", context)


def about(request):
    context = {}
    return render (request, "broker/about.html", context)


def contact(request):
    context = {}
    return render (request, "broker/contact.html", context)

def contact_us(request):
    context = {}
    return render (request, "broker/contact-us.html", context)

def education(request):
    context = {}
    return render (request, "broker/education.html", context)

def faq(request):
    context = {}
    return render (request, "broker/faq.html", context)

def news(request):
    context = {}
    return render (request, "broker/news.html", context)


def privacy_policy(request):
    context = {}
    return render (request, "broker/privacy-policy.html", context)


def privacy(request):
    context = {}
    return render (request, "broker/privacy.html", context)


def terms_and_condition(request):
    context = {}
    return render (request, "broker/terms-and-condition.html", context)


def template_activate_account(request):
    context = {}
    return render (request, "broker/template-activate-account.html", context)
    
def support(request):
    context = {}
    return render (request, "broker/support.html", context)

def investments(request):
    context = {}
    return render (request, "broker/investments.html", context)

@login_required (login_url = "login")
def change_avatar(request):
    profile = request.user.profile
    form = ProfileForm (instance = profile)

    if request.method == 'POST':
        form = ProfileForm (request.POST, request.FILES, instance = profile)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "broker/change-avatar.html", context)

@login_required (login_url = "login")
def change_password(request):
    context = {}
    return render (request, "broker/change-password.html", context)

@login_required (login_url = "login")
def crypto(request):
    context = {}
    return render (request, "broker/crypto.html", context)

@login_required (login_url = "login")
def dashboard(request):
    context = {}
    return render (request, "broker/dashboard.html", context)

@login_required (login_url = "login")
def deposit(request):
    context = {}
    return render (request, "broker/deposit.html", context)

@login_required (login_url = "login")
def fund_transfer(request):
    context = {}
    return render (request, "broker/fund-transfer.html", context)

@login_required (login_url = "login")
def kyc_form(request):
    verify = request.user.verify
    form = VerifyForm (instance = verify)

    if request.method == 'POST':
        form = VerifyForm (request.POST, request.FILES, instance = verify)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "broker/kyc-form.html", context)

@login_required (login_url = "login")
def kyc(request):
    context = {}
    return render (request, "broker/kyc.html", context)

@login_required (login_url = "login")
def market(request):
    context = {}
    return render (request, "broker/market.html", context)

@login_required (login_url = "login")
def settings(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "broker/settings.html", context)


@login_required (login_url = "login")
def signal(request):
    context = {}
    return render (request, "broker/signal.html", context)

@login_required (login_url = "login")
def trade_history(request):
    context = {}
    return render (request, "broker/trade-history.html", context)


def verify(request):
    context = {}
    return render (request, "broker/verify.html", context)

@login_required (login_url = "login")
def withdrawal_info(request):
    account = request.user.account
    form = AccountForm (instance = account)

    if request.method == 'POST':
        form = AccountForm (request.POST, request.FILES, instance = account)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "broker/withdrawal-info.html", context)

@login_required (login_url = "login")
def withdrawal(request):
    context = {}
    return render (request, "broker/withdrawal.html", context)

@unauthenticated_user
def register(request):
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            username = form.cleaned_data.get ('username')


            messages.success (request, 'Account was created for ' + username)

            return redirect ('login')

    context = {'form': form}
    return render (request, "broker/register.html", context)


def logoutUser(request):
    logout (request)
    return redirect ('login')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect ('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate (request, username = username, password = password)

            if user is not None:
                login (request, user)
                return redirect ('dashboard')
            else:
                messages.info (request, 'Username OR password is incorrect')

        context = {}
    return render (request, "broker/login.html", context)

@login_required (login_url = "login")
def reset_password( request):
    return render (request, 'broker/reset-password.html') 


@unauthenticated_user
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("broker/template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('login')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="broker/reset-password.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'broker/change-password.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("login")


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('login')



def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("broker/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def template_activate_account(request):
    context = {}
    return render (request, "broker/template-activate-account.html", context)


@login_required (login_url = "login")
def pin(request):
    context = {}
    return render (request, "broker/pin.html", context)


@login_required (login_url = "login")
def processing(request):
    context = {}
    return render (request, "broker/processing.html", context)