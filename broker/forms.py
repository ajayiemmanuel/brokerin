from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'name']


class ProfileForm (ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'name']

class AccountForm (ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['user', 'name']


class DepositForm (ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = ['user']


class TransactionForm (ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['user']


class TransactiononeForm (ModelForm):
    class Meta:
        model = Transactionone
        fields = '__all__'
        exclude = ['user']


class TransactiontwoForm (ModelForm):
    class Meta:
        model = Transactiontwo
        fields = '__all__'
        exclude = ['user']



class TransactionthreeForm (ModelForm):
    class Meta:
        model = Transactionthree
        fields = '__all__'
        exclude = ['user']


class WalletForm (ModelForm):
    class Meta:
        model = Wallet
        fields = '__all__'
        exclude = ['user']


class PinForm (ModelForm):
    class Meta:
        model = Pin
        fields = '__all__'
        exclude = ['user', 'name']

class ReportForm (ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['user']


class AlertForm (ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'
        exclude = ['user']


class VerifyForm (ModelForm):
    class Meta:
        model = Verify
        fields = '__all__'
        exclude = ['user']